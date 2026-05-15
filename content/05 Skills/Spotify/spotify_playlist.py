"""
spotify_playlist.py — Rafa AI Brain
Cria ou atualiza playlists no Spotify a partir de uma lista de músicas.

Uso:
  python3 spotify_playlist.py --name "Nome da Playlist" --songs "Artista - Música" "Artista - Música" ...
  python3 spotify_playlist.py --name "Nome da Playlist" --file songs.txt
  python3 spotify_playlist.py --list   (lista playlists existentes)
"""

import argparse
import base64
import json
import os
import sys
import requests

CREDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spotify_creds.json")


# ─── Auth ────────────────────────────────────────────────────────────────────

def load_creds():
    if not os.path.exists(CREDS_FILE):
        print("❌ spotify_creds.json não encontrado. Rode o spotify_auth.py primeiro.")
        sys.exit(1)
    with open(CREDS_FILE) as f:
        return json.load(f)


def get_access_token(creds):
    credentials = base64.b64encode(
        f"{creds['client_id']}:{creds['client_secret']}".encode()
    ).decode()
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": creds["refresh_token"],
        },
    )
    data = response.json()
    if "access_token" not in data:
        print(f"❌ Erro ao renovar token: {data}")
        sys.exit(1)
    return data["access_token"]


def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


# ─── Spotify API ──────────────────────────────────────────────────────────────

def get_user_id(token):
    r = requests.get("https://api.spotify.com/v1/me", headers=headers(token))
    return r.json()["id"]


def me_headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def search_track(token, query):
    """Busca uma faixa no Spotify. Query no formato 'Artista - Música' ou livre."""
    r = requests.get(
        "https://api.spotify.com/v1/search",
        headers=headers(token),
        params={"q": query, "type": "track", "limit": 1},
    )
    items = r.json().get("tracks", {}).get("items", [])
    if not items:
        return None
    track = items[0]
    return {
        "uri": track["uri"],
        "name": track["name"],
        "artist": track["artists"][0]["name"],
        "id": track["id"],
    }


def get_existing_playlist(token, playlist_name):
    """Retorna a playlist existente com esse nome (ou None)."""
    url = "https://api.spotify.com/v1/me/playlists"
    while url:
        r = requests.get(url, headers=headers(token), params={"limit": 50})
        data = r.json()
        for pl in data.get("items", []):
            if pl and pl.get("name") == playlist_name:
                return pl
        url = data.get("next")
    return None


def create_playlist(token, name, description=""):
    r = requests.post(
        "https://api.spotify.com/v1/me/playlists",
        headers=headers(token),
        json={"name": name, "description": description, "public": False},
    )
    return r.json()


def clear_playlist(token, playlist_id):
    """Remove todas as faixas de uma playlist."""
    # Pega todas as faixas atuais
    uris = []
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/items"
    while url:
        r = requests.get(url, headers=headers(token), params={"limit": 100})
        data = r.json()
        for item in data.get("items", []):
            if item and item.get("track") and item["track"].get("uri"):
                uris.append({"uri": item["track"]["uri"]})
        url = data.get("next")
    if uris:
        # Remove em lotes de 100
        for i in range(0, len(uris), 100):
            requests.delete(
                f"https://api.spotify.com/v1/playlists/{playlist_id}/items",
                headers=headers(token),
                json={"tracks": uris[i:i+100]},
            )


def add_tracks_to_playlist(token, playlist_id, uris):
    """Adiciona faixas à playlist em lotes de 100."""
    for i in range(0, len(uris), 100):
        r = requests.post(
            f"https://api.spotify.com/v1/playlists/{playlist_id}/items",
            headers=headers(token),
            json={"uris": uris[i:i+100]},
        )
        if r.status_code not in [200, 201]:
            print(f"  ⚠️ Erro ao adicionar lote {i//100+1}: {r.status_code} {r.text[:200]}")


def list_playlists(token):
    playlists = []
    url = "https://api.spotify.com/v1/me/playlists"
    while url:
        r = requests.get(url, headers=headers(token), params={"limit": 50})
        data = r.json()
        for pl in data.get("items", []):
            if pl:
                playlists.append(pl)
        url = data.get("next")
    return playlists


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gerencia playlists do Spotify — Rafa AI Brain")
    parser.add_argument("--name", help="Nome da playlist")
    parser.add_argument("--songs", nargs="+", help='Lista de músicas no formato "Artista - Música"')
    parser.add_argument("--file", help="Arquivo .txt com uma música por linha")
    parser.add_argument("--list", action="store_true", help="Lista suas playlists")
    parser.add_argument("--description", default="Gerada pelo Rafa AI Brain", help="Descrição da playlist")
    args = parser.parse_args()

    creds = load_creds()
    token = get_access_token(creds)

    # ── Listar playlists ──
    if args.list:
        playlists = list_playlists(token)
        print(f"\n🎵 Suas playlists ({len(playlists)}):\n")
        for pl in playlists:
            count = pl.get("tracks", {}).get("total", "?")
            print(f"  • {pl['name']} ({count} faixas) — {pl['id']}")
        return

    # ── Criar/atualizar playlist ──
    if not args.name:
        parser.print_help()
        sys.exit(1)

    # Coleta as músicas
    songs = []
    if args.songs:
        songs = args.songs
    elif args.file:
        with open(args.file) as f:
            songs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        print("❌ Informe --songs ou --file com as músicas.")
        sys.exit(1)

    print(f"\n🎵 Processando playlist: '{args.name}'")
    print(f"📋 {len(songs)} músicas para buscar\n")

    # Busca cada música
    found_uris = []
    not_found = []

    for song in songs:
        result = search_track(token, song)
        if result:
            found_uris.append(result["uri"])
            print(f"  ✅ {result['artist']} — {result['name']}")
        else:
            not_found.append(song)
            print(f"  ❌ Não encontrado: {song}")

    print(f"\n📊 Resultado: {len(found_uris)} encontradas, {len(not_found)} não encontradas")

    if not found_uris:
        print("❌ Nenhuma música encontrada. Playlist não criada.")
        sys.exit(1)

    # Verifica se a playlist já existe
    existing = get_existing_playlist(token, args.name)

    if existing:
        playlist_id = existing["id"]
        print(f"\n🔄 Playlist '{args.name}' já existe — atualizando...")
        clear_playlist(token, playlist_id)
    else:
        print(f"\n✨ Criando playlist '{args.name}'...")
        new_pl = create_playlist(token, args.name, args.description)
        playlist_id = new_pl["id"]

    add_tracks_to_playlist(token, playlist_id, found_uris)

    playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
    print(f"\n✅ Playlist pronta! → {playlist_url}")

    if not_found:
        print(f"\n⚠️  Músicas não encontradas:")
        for s in not_found:
            print(f"   • {s}")


if __name__ == "__main__":
    main()

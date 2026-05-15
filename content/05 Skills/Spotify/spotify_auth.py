"""
spotify_auth.py — Rafa AI Brain
Autentica com o Spotify e salva o refresh token para uso futuro.
Rode uma vez. Depois disso, o spotify_playlist.py cuida de tudo.
"""

import http.server
import urllib.parse
import webbrowser
import json
import base64
import threading
import requests

CLIENT_ID = "b1e246aa2e2143698346051406da42ce"
CLIENT_SECRET = "0c9faca9912b48c3bb139b0317d54654"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "playlist-modify-public playlist-modify-private playlist-read-private"
CREDS_FILE = "spotify_creds.json"

auth_code = None
server_done = threading.Event()


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>✅ Autenticado! Pode fechar essa janela.</h1>".encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"<h1>Erro na autenticacao.</h1>")

        server_done.set()

    def log_message(self, format, *args):
        pass  # silencia logs do servidor HTTP


def get_auth_url():
    params = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
    })
    return f"https://accounts.spotify.com/authorize?{params}"


def exchange_code_for_tokens(code):
    credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
    )
    return response.json()


if __name__ == "__main__":
    print("🎵 Spotify Auth — Rafa AI Brain")
    print("Iniciando servidor local na porta 8888...")

    server = http.server.HTTPServer(("127.0.0.1", 8888), CallbackHandler)
    server_thread = threading.Thread(target=server.handle_request)
    server_thread.daemon = True
    server_thread.start()

    auth_url = get_auth_url()
    print(f"Abrindo navegador para autenticação...")
    webbrowser.open(auth_url)

    print("Aguardando callback do Spotify...")
    server_done.wait(timeout=120)

    if auth_code:
        print("✅ Código recebido! Trocando por tokens...")
        tokens = exchange_code_for_tokens(auth_code)

        if "refresh_token" not in tokens:
            print(f"❌ Erro ao obter tokens: {tokens}")
            exit(1)

        creds = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": tokens["refresh_token"],
        }

        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        creds_path = os.path.join(script_dir, CREDS_FILE)

        with open(creds_path, "w") as f:
            json.dump(creds, f, indent=2)

        print(f"✅ Credenciais salvas em: {creds_path}")
        print("Autenticação concluída! Agora você pode usar o spotify_playlist.py")
    else:
        print("❌ Timeout ou falha na autenticação. Tente novamente.")

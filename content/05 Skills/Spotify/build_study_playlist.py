#!/usr/bin/env python3
"""
build_study_playlist.py — Builds the Artist Study List playlist on Spotify.
Searches each song with artist field filter, adds to playlist using /items endpoint.
Handles rate limits gracefully.
"""
import requests, json, base64, time, sys, os

CREDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spotify_creds.json")
PLAYLIST_ID = "243ICRrTadWHTf0rND5IlL"

# Exact songs from Artist Study List
SONGS = [
    # Study Queue
    ("Fred again..","Jungle"),("Kanye West","Runaway"),
    # Pop / Alternative Pop
    ("Billie Eilish","when the party's over"),("Billie Eilish","lovely"),("Billie Eilish","ocean eyes"),
    ("Bruno Mars","Perm"),("Bruno Mars","Finesse"),("Bruno Mars","That's What I Like"),
    ("The Weeknd","Blinding Lights"),("The Weeknd","Often"),("The Weeknd","Die For You"),
    ("Olivia Rodrigo","drivers license"),("Olivia Rodrigo","brutal"),("Olivia Rodrigo","vampire"),
    ("Dua Lipa","Levitating"),("Dua Lipa","Physical"),("Dua Lipa","Don't Start Now"),
    ("Charli XCX","Speed Drive"),("Charli XCX","Von dutch"),("Charli XCX","360"),
    ("Harry Styles","Watermelon Sugar"),("Harry Styles","As It Was"),("Harry Styles","Matilda"),
    ("Lana Del Rey","West Coast"),("Lana Del Rey","Video Games"),("Lana Del Rey","Summertime Sadness"),
    # R&B / Soul
    ("Frank Ocean","Nights"),("Frank Ocean","Ivy"),("Frank Ocean","Self Control"),
    ("SZA","Kill Bill"),("SZA","Good Days"),("SZA","The Weekend"),
    ("Daniel Caesar","Get You"),("Daniel Caesar","Best Part"),("Daniel Caesar","Blessed"),
    ("Brent Faiyaz","Clouded"),("Brent Faiyaz","Dead Man Walking"),("Brent Faiyaz","Gravity"),
    ("D'Angelo","Untitled"),("D'Angelo","Brown Sugar"),("D'Angelo","Devil's Pie"),
    # Hip-Hop / Trap
    ("Kanye West","All Falls Down"),("Kanye West","New Slaves"),
    ("Metro Boomin","Superhero"),("Metro Boomin","Calling My Name"),("Metro Boomin","Creepin'"),
    ("Tyler, the Creator","EARFQUAKE"),("Tyler, the Creator","See You Again"),("Tyler, the Creator","NEW MAGIC WAND"),
    ("Travis Scott","SICKO MODE"),("Travis Scott","goosebumps"),("Travis Scott","HIGHEST IN THE ROOM"),
    ("Drake","Passionfruit"),("Drake","Marvin's Room"),("Drake","From Time"),
    ("Kendrick Lamar","PRIDE."),("Kendrick Lamar","Money Trees"),("Kendrick Lamar","Alright"),
    ("J. Cole","No Role Modelz"),("J. Cole","Love Yourz"),("J. Cole","She Knows"),
    ("Future","March Madness"),("Future","Mask Off"),("Future","Life Is Good"),
    # Electronic / Club / UK
    ("Fred again..","Danielle"),("Fred again..","Bleu"),
    ("Four Tet","Baby"),("Four Tet","Two Thousand and Seventeen"),("Four Tet","My Angel Rocks Back and Forth"),
    ("James Blake","Retrograde"),("James Blake","The Wilhelm Scream"),("James Blake","Limit to Your Love"),
    ("Kaytranada","You're the One"),("Kaytranada","WHAT YOU NEED"),("Kaytranada","10%"),
    ("Disclosure","Latch"),("Disclosure","You & Me"),("Disclosure","Magnets"),
    # Musica Brasileira
    ("Anitta","Funk Rave"),("Anitta","Envolver"),("Anitta","Downtown"),
    ("Luisa Sonza","Chico"),("Luisa Sonza","Flores"),("Luisa Sonza","To Bem"),
    # Afrobeats / Amapiano
    ("Tyla","Water"),("Tyla","Getting Late"),("Tyla","Playtime"),
    ("Wizkid","Essence"),("Wizkid","Master Groove"),
    ("Burna Boy","Last Last"),("Burna Boy","ye"),
    # Indie Pop / Alternative
    ("Clairo","Bags"),("Clairo","Amoeba"),("Clairo","Sofia"),
    ("Mac DeMarco","Chamber of Reflection"),("Mac DeMarco","My Kind of Woman"),("Mac DeMarco","Still Together"),
    ("Boygenius","Not Strong Enough"),("Boygenius","the record"),("Boygenius","salt"),
    ("Phoebe Bridgers","Scott Street"),("Phoebe Bridgers","Kyoto"),
    ("Snail Mail","Heat Wave"),("Snail Mail","Lush"),("Snail Mail","Romantic Comedy"),
    # Ambient / Experimental
    ("Brian Eno","An Ending Ascent"),("Brian Eno","Music for Airports"),
    ("Jon Hopkins","Open Eye Signal"),("Jon Hopkins","Emerald Rush"),
    ("Arca","Nonbinary"),
    ("Aphex Twin","Come to Daddy"),("Aphex Twin","Windowlicker"),("Aphex Twin","Vordhosbn"),
    # Synthwave / Synthpop
    ("The Midnight","Los Angeles"),("The Midnight","Crystalline"),("The Midnight","The Unraveling"),
    ("Perturbator","Assault"),("Perturbator","Night Driving Retrospective"),("Perturbator","Deus Ex Machina"),
    ("Chvrches","The Mother We Share"),("Chvrches","Clearest Blue"),("Chvrches","Recover"),
    # Latin Trap
    ("Bad Bunny","Dakiti"),("Bad Bunny","Titi Me Pregunto"),("Bad Bunny","Ella Baila Sola"),
    ("Rauw Alejandro","Punto G"),("Rauw Alejandro","Cosa Guapa"),("Rauw Alejandro","Ella Baila Sola"),
    # Reggaeton / Urban
    ("Daddy Yankee","Gasolina"),("Daddy Yankee","Despacito"),
    ("J Balvin","Mi Gente"),("J Balvin","Telefono"),("J Balvin","IN DA GHETTO"),
    ("Rosalia","Malamente"),("Rosalia","Aute Cuture"),("Rosalia","Despecha"),
    # Classicos
    ("Michael Jackson","Billie Jean"),("Michael Jackson","Thriller"),("Michael Jackson","Human Nature"),
    ("Prince","Kiss"),("Prince","When Doves Cry"),("Prince","Purple Rain"),
    ("Stevie Wonder","Superstition"),("Stevie Wonder","Isn't She Lovely"),("Stevie Wonder","Pastime Paradise"),
]

def get_token():
    creds = json.load(open(CREDS_FILE))
    credentials = base64.b64encode(f"{creds['client_id']}:{creds['client_secret']}".encode()).decode()
    r = requests.post("https://accounts.spotify.com/api/token",
        headers={"Authorization": f"Basic {credentials}", "Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "refresh_token", "refresh_token": creds["refresh_token"]})
    return r.json()["access_token"]

def search(h, artist, track):
    for q in [f"artist:{artist} track:{track}", f"{artist} {track}"]:
        try:
            r = requests.get("https://api.spotify.com/v1/search", headers=h,
                params={"q": q, "type": "track", "limit": 5}, timeout=10)
            if r.status_code == 429:
                w = min(int(r.headers.get("Retry-After", 5)), 30)
                print(f"  [rate limit, waiting {w}s]", flush=True)
                time.sleep(w)
                r = requests.get("https://api.spotify.com/v1/search", headers=h,
                    params={"q": q, "type": "track", "limit": 5}, timeout=10)
            if r.status_code != 200:
                continue
            for item in r.json().get("tracks",{}).get("items",[]):
                ia = [a["name"].lower() for a in item["artists"]]
                if any(artist.lower() in a or a in artist.lower() for a in ia):
                    return item
        except Exception as e:
            time.sleep(2)
    return None

def main():
    token = get_token()
    h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Check if we have cached results
    cache_file = "/tmp/study_playlist_cache.json"
    if os.path.exists(cache_file):
        cached = json.load(open(cache_file))
        uris = cached["uris"]
        nf = cached["not_found"]
        print(f"Using cached results: {len(uris)} found, {len(nf)} missing", flush=True)
    else:
        uris, nf = [], []
        for i,(a,t) in enumerate(SONGS):
            r = search(h, a, t)
            if r:
                name = ", ".join(x["name"] for x in r["artists"])
                print(f"[{i+1}/{len(SONGS)}] OK {name} - {r['name']}", flush=True)
                uris.append(r["uri"])
            else:
                print(f"[{i+1}/{len(SONGS)}] XX {a} - {t}", flush=True)
                nf.append(f"{a} - {t}")
            time.sleep(0.5)

        # Cache results
        json.dump({"uris": uris, "not_found": nf}, open(cache_file, "w"))

    print(f"\nFound: {len(uris)} / Missing: {len(nf)}", flush=True)
    for s in nf:
        print(f"  MISSING: {s}", flush=True)

    # Clear and rebuild playlist
    print(f"\nClearing playlist {PLAYLIST_ID}...", flush=True)
    cur_url = f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/items"
    current = []
    while cur_url:
        r = requests.get(cur_url, headers=h, params={"limit": 100}, timeout=10)
        if r.status_code != 200: break
        data = r.json()
        for item in data.get("items", []):
            if item and item.get("track") and item["track"].get("uri"):
                current.append({"uri": item["track"]["uri"]})
        cur_url = data.get("next")

    if current:
        for j in range(0, len(current), 100):
            requests.delete(f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/items", headers=h,
                json={"tracks": current[j:j+100]}, timeout=10)
        print(f"  Removed {len(current)} tracks", flush=True)

    # Add tracks
    print(f"Adding {len(uris)} tracks...", flush=True)
    for j in range(0, len(uris), 100):
        batch = uris[j:j+100]
        r = requests.post(f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/items", headers=h,
            json={"uris": batch}, timeout=10)
        print(f"  Batch {j//100+1}: {r.status_code}", flush=True)
        time.sleep(0.5)

    # Verify
    time.sleep(1)
    r = requests.get(f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/items?limit=1", headers=h, timeout=10)
    if r.status_code == 200:
        print(f"\nPlaylist: {r.json()['total']} tracks", flush=True)
    print(f"https://open.spotify.com/playlist/{PLAYLIST_ID}", flush=True)

if __name__ == "__main__":
    main()

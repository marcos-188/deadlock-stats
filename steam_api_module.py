import http.client
import json
import re
api_key = "EB499D551A2B30C4A4802CBB41D71C34"


def steam_id_scrapper(profil):
    profil = profil.rstrip('/')
    steamid64 = None

    if '/profiles/' in profil:
        match = re.search(r'/profiles/(\d+)', profil)
        if match:
            steamid64 = int(match.group(1))
            return steamid64
        else:
            return f"Wystąpił błąd prawdopodobnie podano zły link. \nPodaj pełny link do profilu Steam."

    elif '/id/' in profil:
        match = re.search(r'/id/(\S+)', profil)
        if match:
            vanity_url = str(match.group(1))
            url = f"/ISteamUser/ResolveVanityURL/v0001?key={api_key}&vanityurl={vanity_url}"
            conn = http.client.HTTPSConnection("api.steampowered.com")
            conn.request("GET", url)
            dane = json.loads(conn.getresponse().read().decode('utf-8'))
            return int(dane['response']['steamid'])
        else:
            return f"Wystąpił błąd prawdopodobnie podano zły link. \nPodaj pełny link do profilu Steam."
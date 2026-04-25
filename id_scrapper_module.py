import http.client
import json
import urllib.parse
import re

def steam_id_scrapper(profil):
    profil = profil.rstrip('/')
    steamid64 = None

    if '/profiles/' in profil:
        match = re.search(r'/profiles/(\d+)', profil)
        if match:
            steamid64 = int(match.group(1))
    elif '/id/' in profil:
        try:
            # Rozbijamy URL na domenę i ścieżkę dla http.client
            parsed_url = urllib.parse.urlparse(profil)

            # Nawiązujemy bezpieczne połączenie (HTTPS)
            conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=5)
            conn.request("GET", parsed_url.path)
            response = conn.getresponse()

            if response.status == 200:
                html_content = response.read().decode('utf-8', errors='ignore')

                # Szukamy ukrytego bloku JSON w kodzie źródłowym (g_rgProfileData)
                match = re.search(r'g_rgProfileData\s*=\s*({.*?});', html_content)

                if match:
                    profile_data = json.loads(match.group(1))
                    steamid64 = int(profile_data.get('steamid'))
                else:
                    return "Nie znaleziono danych w kodzie strony. Profil może nie istnieć."
            else:
                return f"Błąd połączenia. Kod statusu HTTP: {response.status}"

            conn.close()

        except Exception as e:
            return f"Wystąpił błąd podczas komunikacji: {e}"
    return steamid64 - 76561197960265728
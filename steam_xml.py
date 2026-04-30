import http.client
import urllib.parse
import xml.etree.ElementTree as ET

def steam_id_finder(profil):
    profil = profil.rstrip('/')
    url=f"{profil}?xml=1"

    try:
        parsed_url = urllib.parse.urlparse(url)
        conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=2)
        full_path = f"{parsed_url.path}?{parsed_url.query}"
        conn.request("GET", full_path)
        response = conn.getresponse()
        if response.status == 200:
            dane = response.read()
            root = ET.fromstring(dane)
            steamid64 = root.find("steamID64").text
            if steamid64 is not None:
                return (int(steamid64))
            else:
                return "Nie znaleziono danych, upewnij się że link jest poprawny"
        else:
            return f"Błąd połączenia. Kod statusu HTTP: {response.status}."
    except Exception as e:
        return f"Wystąpił błąd - {e}"
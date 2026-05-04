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
            root = ET.fromstring(response.read())
            steamid64 = root.find("steamID64").text
            if steamid64 is not None:
                return (int(steamid64))
            else:
                return "Nie znaleziono danych, upewnij się że link jest poprawny"
        else:
            return f"Błąd połączenia. Kod statusu HTTP: {response.status}."
    except Exception as e:
        return f"Wystąpił błąd - {e}"

def steam_profile_data_finder(steamid64):
    try:
        conn = http.client.HTTPSConnection("steamcommunity.com", timeout=2)
        conn.request("GET", f"/profiles/{steamid64}?xml=1")
        response = conn.getresponse()
        if response.status == 200:
            root = ET.fromstring(response.read())
            profile_name = root.find("steamID").text
            profile_pic = root.find("avatarFull").text
            return profile_name, profile_pic
        else:
            return "Nie znaleziono danych, upewnij się że link jest poprawny"

    except Exception as e:
        return f"Wystąpił błąd - {e}"

#print(steam_profile_data_finder(steam_id_finder('https://steamcommunity.com/id/marcos-zagorz')))
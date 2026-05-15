import os, shutil
from pathlib import Path
import urllib.request
from PySide6.QtGui import QPixmap
import http.client
import json
import requests
addres = '13.60.230.106'

#pobieranie z api i inne funkcje

def get_app_dir(nazwa_programu):
    katalog_domowy = Path.home()
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / nazwa_programu
    else:
        return katalog_domowy / "AppData" / "Roaming" / nazwa_programu

def usun_cache():
    folder = get_app_dir("DeadlockStats")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def load_image_from_url(url, label):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
    except Exception as e:
        print(f"Nie udało się załadować obrazka: {e}")
        label.setText("Błąd ładowania obrazka")

def pobierz_gry(steam_id, czy_brawl):
    conn = http.client.HTTPSConnection("api.deadlock-api.com")
    conn.request("GET", f"/v1/players/{steam_id}/match-history?force_refetch=false")
    response = conn.getresponse()
    dane_json = json.loads(response.read().decode('utf-8'))
    if czy_brawl == 0: #zależnie od wyboru użytkownika odrzuca gry Brawl, pobiera wszystkie albo pobiera tylko Brawl
        dane = [x for x in dane_json if x.get('game_mode') == 1]
    elif czy_brawl == 2:
        dane = [x for x in dane_json if x.get('game_mode') == 4]
    else:
        dane = dane_json
    conn.close()
    return dane

def pobierz_steam_z_api(link):
    url = f"http://{addres}:6969/steamdata/"
    params = {"link": link}
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # }
    odpowiedz = requests.get(url, params=params,  timeout=5)
    if odpowiedz.status_code == 200:
        dane = odpowiedz.json()
        steamid = dane['steamid']
        profname = dane['profname']
        profpic = dane['profpic']
        return steamid, profname, profpic
    elif odpowiedz.status_code == 400:
        raise ValueError(f"Nie udało się pobrać ID: {odpowiedz.json()['details']}")
    return None

def pobierz_postacie_z_api():
    url = f"http://{addres}:6969/heroes"
    odpowiedz = requests.get(url, timeout=5)
    if odpowiedz.status_code == 200:
        dane = odpowiedz.json()
        return dane
    else:
        raise ValueError(f"Nie udało się pobrać ID: {odpowiedz.json()['details']}")
    return None
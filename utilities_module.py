import sys
import os
from pathlib import Path
import urllib.request
from PySide6.QtGui import QPixmap
import http.client
import json
import requests
import pickle

def get_app_dir(nazwa_programu):
    katalog_domowy = Path.home()
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / nazwa_programu
    else:
        return katalog_domowy / "AppData" / "Roaming" / nazwa_programu

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

def pobierz_gry(gry_count, steam_id, czy_brawl):
    conn = http.client.HTTPSConnection("api.deadlock-api.com")
    conn.request("GET", f"/v1/players/{steam_id}/match-history?force_refetch=false")
    response = conn.getresponse()
    surowe_dane = response.read().decode('utf-8')
    if czy_brawl == 0: #zależnie od wyboru użytkownika odrzuca gry Brawl, pobiera wszystkie albo pobiera tylko Brawl
        dane = [x for x in json.loads(surowe_dane) if x.get('game_mode') == 1]
    elif czy_brawl == 2:
        dane = [x for x in json.loads(surowe_dane) if x.get('game_mode') == 4]
    else:
        dane = json.loads(surowe_dane)
    if gry_count > len(dane) or gry_count == 0: #jeżeli nie ma aż tylu gier albo wybrano wszystkie zwraca wszystko co znajdzie
        gry_count = len(dane)
    zwrot = dane[:gry_count]
    conn.close()
    return zwrot

def pobierz_postacie():
    plik_zapisu = get_app_dir("DeadlockStats") / "postacie.pkl"
    if plik_zapisu.exists():
        with open(plik_zapisu, 'rb') as plik:
            return pickle.load(plik)
    else:
        url = "https://assets.deadlock-api.com/v2/heroes"
        params = {
            "language": "english",
            "client_version": "6484",
            "only_active": "true"
        }
        response = requests.get(url, params=params)

        heroes_data = response.json()

        hero_dict = {
            hero.get('id'):
            {
                "name": hero.get("name"),
                "icon": hero.get("images", {}).get("minimap_image_webp")
            }
            for hero in heroes_data if hero.get("id") is not None
        }

        with open(plik_zapisu, 'wb') as plik:
            pickle.dump(hero_dict, plik)

        return hero_dict

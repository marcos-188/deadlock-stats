import http.client
import json
import requests
from utilities_module import get_app_dir

from steam_xml import steam_id_finder

def pobierz_gry(gry_count, steam_id, czy_brawl): #pobieranie danych z deadlock-api
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
    plik_zapisu = get_app_dir("DeadlockStats") / "postacie.json"
    if plik_zapisu.exists():
        with open(plik_zapisu, 'r', encoding='utf-8') as plik:
            return json.load(plik)
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

        with open(plik_zapisu, 'w', encoding='utf-8') as plik:
            json.dump(hero_dict, plik, ensure_ascii=False, indent=4)

        return hero_dict

def avg_stat(stat, gry):
    suma = 0
    for gra in gry:
        if gra[stat]:
            suma += gra[stat]
        else:
            suma += 0
    return round(suma / len(gry),2)

def max_stat(stat, gry):
    max_s = 0
    for gra in gry:
        if gra[stat]:
            if gra[stat] > max_s:
                max_s = gra[stat]
    return max_s

def oblicz_winrate(gry):
    win = 0
    for gra in gry:
        if gra['player_team'] == gra['match_result']:
            win += 1
    return round(win / len(gry) * 100, 2)

def wypisz_statystyki(gry):
    return (f'''Statystyki z ostatnich {len(gry)} gier :
    \nŚrednia zabójstw : {avg_stat('player_kills',gry)}
    \nŚrednia śmierci : {avg_stat('player_deaths',gry)}
    \nŚrednia asyst : {avg_stat('player_assists',gry)}
    \nK/D : {round(avg_stat('player_kills',gry)/avg_stat('player_deaths',gry),2)}
    \nWin rate : {oblicz_winrate(gry)}
    \nŚredni czas gry : {round(avg_stat('match_duration_s',gry)/60,2)} minut''')
import http.client
import json
from id_scrapper_module import steam_id_scrapper

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

def avg_stat(stat, gry):
    suma = 0
    for gra in gry:
        suma += gra[stat]
    return round(suma / len(gry),2)

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

def steam_id_find():
    while True:
        wynik = steam_id_scrapper(input("Podaj link do profilu steam : "))
        if isinstance(wynik, int):
            return wynik
        else:
            print(f"Błąd. {wynik}")

def steam_id_find_gui(steam_link):
    wynik = steam_id_scrapper(steam_link)
    if isinstance(wynik, int):
        return wynik
    else:
        raise ValueError(f"Nie udało się pobrać ID: {wynik}")

def main():
    print("Statystyki Deadlock dla biednych :)")
    gry_count = int(input("Z ilu ostatnich gier pobrać dane : "))
    steam_id = steam_id_find()
    czy_brawl = int(input("Czy liczyć gry Brawl (0 - nie, 1 - tak, 2 - tylko brawl : "))
    ostatnie_gry = pobierz_gry(gry_count, steam_id, czy_brawl)
    wypisz_statystyki(ostatnie_gry)
    input("Nacisnij cokolwiek aby zamknąć")

if __name__ == "__main__":
    main()

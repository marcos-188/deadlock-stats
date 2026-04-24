import http.client
import json

def pobierz_gry(gry_count, steam_id, czy_brawl):
    conn = http.client.HTTPSConnection("api.deadlock-api.com")
    conn.request("GET", f"/v1/players/{steam_id}/match-history?force_refetch=false")
    response = conn.getresponse()
    surowe_dane = response.read().decode('utf-8')
    if czy_brawl == 0:
        dane = [x for x in json.loads(surowe_dane) if x.get('game_mode') == 1]
    elif czy_brawl == 2:
        dane = [x for x in json.loads(surowe_dane) if x.get('game_mode') == 4]
    else:
        dane = json.loads(surowe_dane)
    if gry_count > len(dane):
        gry_count = len(dane)
    zwrot = dane[:gry_count]
    conn.close()
    return zwrot
#asas
def avg_stat(stat, gry):
    suma = 0
    for gra in gry:
        suma += gra[stat]
        #print(f"debug - gra {gra['match_id']}, stat{gra[stat]}")
    return round(suma / len(gry),2)

def oblicz_winrate(gry):
    win = 0
    for gra in gry:
        if gra['player_team'] == gra['match_result']:
            win += 1
    return round(win / len(gry) * 100, 2)
        #print(gra['match_id'])
        #print(gra['match_result'])
        #print(gra['player_team'])

def wypisz_staty(gry):
    print(f"Statystyki z ostatnich {len(gry)} gier : ")
    print(f"Średnia zabójstw : {avg_stat('player_kills',gry)}")
    print(f"Średnia śmierci : {avg_stat('player_deaths',gry)}")
    print(f"Średnia asyst : {avg_stat('player_assists',gry)}")
    print(f"K/D : {round(avg_stat('player_assists',gry)/avg_stat('player_deaths',gry),2)}")
    print(f"Win rate : {oblicz_winrate(gry)}")
    print(f"Średni czas gry : {round(avg_stat('match_duration_s',gry)/60,2)} minut")
    print()

def main():
    print("Statystyki Deadlock dla biednych :)")
    gry_count = int(input("Z ilu ostatnich gier pobrać dane : "))
    steam_id = input("Podaj SteamID32: ")
    czy_brawl = int(input("Czy liczyć gry Brawl (0 - nie, 1 - tak, 2 - tylko brawl : "))

    ostatnie_gry = pobierz_gry(gry_count, steam_id, czy_brawl)
    wypisz_staty(ostatnie_gry)
    #print(ostatnie_gry)

    input("Nacisnij cokolwiek aby zamknąć")

if __name__ == "__main__":
    main()

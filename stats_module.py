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
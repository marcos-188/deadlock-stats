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

def kda(gry):
    k = 0
    d = 0
    a = 0
    for gra in gry:
        k += gra['player_kills']
        d += gra['player_deaths']
        a += gra['player_assists']
    return [k, d, a]

def oblicz_winrate(gry):
    win = 0
    loss = 0
    for gra in gry:
        if gra['player_team'] == gra['match_result']:
            win += 1
        else:
            loss += 1
    return [round(win / len(gry) * 100, 2), win, loss]
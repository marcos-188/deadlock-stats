from datetime import datetime

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget, QMainWindow

from steam_xml import steam_profile_data_finder
from ui_game import Ui_Form_Game
from ui_main import Ui_MainWindow
from ui_profile import Ui_Form_Profile
from ui_overwiew import Ui_Form_Overwiew
from ui_pages import Ui_pagesWidget
from utilities_module import load_image_from_url
from utilities_module import pobierz_gry
from stats_module import oblicz_winrate, kda


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, steamid, postacie, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.steamID64 = steamid
        self.dane_postacie = postacie

        self.profile_widget = ProfileWidget(self.steamID64)
        self.header_layout.addWidget(self.profile_widget)
        self.pages_widget = PagesWidget(self)
        self.gridLayout.addWidget(self.pages_widget)

        self.gry = pobierz_gry(self.steamID64, 0)
        self.numer_gry = 0
        self.ile_gier_na_karte = 5

        self.pages_widget.pushButton_L.clicked.connect(self.lewo)
        self.pages_widget.pushButton_P.clicked.connect(self.prawo)
        self.pages_widget.pushButton_1.clicked.connect(self.zero)

        self.overwiew = OverwiewWidget(self.gry)
        self.overwiew_layout.addWidget(self.overwiew)

        self.zaladuj_gry()

    def zaladuj_gry(self):
        self.clear_layout()
        for n in range(self.ile_gier_na_karte):
            if self.numer_gry >= len(self.gry):
                self.numer_gry = len(self.gry)
                danepostaci = self.dane_postacie.get(self.gry[n+self.numer_gry-self.ile_gier_na_karte]['hero_id'])
                nowe_okno = GameWidget(self.gry[n+self.numer_gry-self.ile_gier_na_karte],danepostaci)
                self.scroll_layout.addWidget(nowe_okno)
            else:
                danepostaci = self.dane_postacie.get(self.gry[n+self.numer_gry]['hero_id'])
                nowe_okno = GameWidget(self.gry[n+self.numer_gry],danepostaci)
                self.scroll_layout.addWidget(nowe_okno)

    def lewo(self):
        if self.numer_gry-5 < 0:
            self.numer_gry = 0
        else:
            self.numer_gry -= 5
        self.zaladuj_gry()

    def prawo(self):
        if self.numer_gry + 5 > len(self.gry):
            self.numer_gry = len(self.gry)
        else:
            self.numer_gry += 5
        self.zaladuj_gry()

    def zero(self):
        self.numer_gry = 0
        self.zaladuj_gry()

    def clear_layout(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


class PagesWidget(QWidget, Ui_pagesWidget):
    def __init__(self, parent=None):
        super(PagesWidget, self).__init__(parent)
        self.setupUi(self)

class ProfileWidget(QWidget, Ui_Form_Profile):
    def __init__(self, steamid ,parent=None):
        super(ProfileWidget, self).__init__(parent)
        self.setupUi(self)
        self.steamID64 = steamid
        self.dane = steam_profile_data_finder(self.steamID64)

        self.label_nazwa.setText(str(self.dane[0]))
        load_image_from_url(self.dane[1], self.label_awatar)

class GameWidget(QWidget, Ui_Form_Game):
    def __init__(self, danegry, danepostaci ,parent=None):
        super(GameWidget, self).__init__(parent)
        self.setupUi(self)

        self.label_heroname.setText(str(danepostaci['name']))
        load_image_from_url(danepostaci['icon'], self.label_heroicon)

        self.label_KDA.setText(f'{danegry["player_kills"]}/{danegry["player_deaths"]}/{danegry["player_assists"]}')
        if danegry['player_team'] == danegry['match_result']:
            self.label_wynik.setText('Zwycięstwo')
            self.label_wynik.setStyleSheet("color: rgb(76, 175, 80)")
        else:
            self.label_wynik.setText("Porażka")
            self.label_wynik.setStyleSheet("color: rgb(221, 63, 51)")
        self.label_Dusze.setText(f'{str(round(danegry['net_worth']/1000,2))}k')
        self.label_idgry.setText("Id: "+str(danegry['match_id']))
        self.label_data.setText("📅"+str(datetime.fromtimestamp(danegry['start_time']).strftime('%Y-%m-%d %H:%M:%S')))
        self.label_duration.setText(f"⏱️ {danegry['match_duration_s']//60}:{danegry['match_duration_s']%60:02d}  min")



class OverwiewWidget(QWidget, Ui_Form_Overwiew):
    def __init__(self, gry, parent=None):
        super(OverwiewWidget, self).__init__(parent)
        self.setupUi(self)

        self.win_loss = oblicz_winrate(gry)
        self.label_winrate.setText(str(self.win_loss[0])+"%")
        if self.win_loss[1]<self.win_loss[2]:
            self.label_winrate.setStyleSheet("color: rgb(221, 63, 51)")
        elif self.win_loss[1]>self.win_loss[2]:
            self.label_winrate.setStyleSheet("color: rgb(76, 175, 80)")
        self.label_WL.setText(f"W:{str(self.win_loss[1])} L:{str(self.win_loss[2])}")

        self.kill_death_assist = kda(gry)
        self.label_KD.setText(str(round(self.kill_death_assist[0]/self.kill_death_assist[1],2)))
        self.label_kkddaa.setText(f'K:{self.kill_death_assist[0]} D:{self.kill_death_assist[1]} A:{self.kill_death_assist[2]}')



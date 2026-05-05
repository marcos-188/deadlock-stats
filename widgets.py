from PySide6.QtWidgets import QWidget, QMessageBox, QMainWindow
from utilities_module import load_image_from_url
from ui_profile import Ui_Form_Profile
from ui_game import Ui_Form_Game
from ui_main import Ui_MainWindow
from steam_xml import steam_profile_data_finder
from datetime import datetime
from stats_module import pobierz_gry

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, steamid, postacie, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.steamID64 = steamid
        self.dane_postacie = postacie
        print(self.dane_postacie[2])
        print(self.steamID64)

        self.profile_widget = ProfileWidget(self.steamID64)
        self.header_layout.addWidget(self.profile_widget)

        self.gry = pobierz_gry(0, self.steamID64, 0)
        for n in range(5):
            danepostaci = self.dane_postacie.get(self.gry[n]['hero_id'])
            nowe_okno = GameWidget(self.gry[n],danepostaci)
            self.scroll_layout.addWidget(nowe_okno)


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
        self.label_duration.setText("⏱️"+str(round(danegry['match_duration_s']/60,2)))


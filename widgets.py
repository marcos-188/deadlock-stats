from PySide6.QtWidgets import QWidget, QMessageBox
from utilities_module import load_image_from_url
from ui_profile import Ui_Form_Profile
from ui_game import Ui_Form_Game
from steam_xml import steam_profile_data_finder


class ProfileWidget(QWidget, Ui_Form_Profile):
    def __init__(self, steamid ,parent=None):
        super(ProfileWidget, self).__init__(parent)
        self.setupUi(self)
        self.steamID64 = steamid
        self.dane = steam_profile_data_finder(self.steamID64)

        self.label_nazwa.setText(str(self.dane[0]))
        load_image_from_url(self.dane[1], self.label_awatar)

class GameWidget(QWidget, Ui_Form_Game):
    def __init__(self, danegry ,parent=None):
        super(GameWidget, self).__init__(parent)
        self.setupUi(self)

        self.label_heroname.setText(str(danegry['hero_id']))
        self.label_KDA.setText(f'{danegry["player_kills"]}/{danegry["player_deaths"]}/{danegry["player_assists"]}')

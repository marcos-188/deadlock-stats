from PySide6.QtWidgets import QWidget, QMessageBox
from utilities_module import load_image_from_url
from ui_profile import Ui_Form_Profile
from steam_xml import steam_profile_data_finder


class ProfileWidget(QWidget, Ui_Form_Profile):
    def __init__(self, steamid ,parent=None):
        super(ProfileWidget, self).__init__(parent)
        self.setupUi(self)
        self.steamID64 = steamid
        self.dane = steam_profile_data_finder(self.steamID64)

        self.label_nazwa.setText(str(self.dane[0]))
        load_image_from_url(self.dane[1], self.label_awatar)

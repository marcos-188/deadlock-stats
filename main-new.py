import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import Signal

from login_window import LoginWindow
from widgets import ProfileWidget
from utilities_module import get_app_dir
#self.plik_zapisu = get_app_dir("DeadlockStats") / "zapisany_steam_id.txt"

#kontroler - uruchamia logowanie i jak przejdzie to otwiera główne okno i zamyka login (chyba xd)
class Controller:
    def __init__(self):
        self.login_window = LoginWindow()
        self.login_window.login_success.connect(self.otworz_profil)

    def start(self):
        self.login_window.show()

    def otworz_profil(self, steamid):
        self.profile_window = ProfileWidget(steamid)
        self.profile_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Inicjalizujemy i uruchamiamy nasz kontroler
    controller = Controller()
    controller.start()

    sys.exit(app.exec())
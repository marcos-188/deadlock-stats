import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import Signal

from login_window import LoginWindow
from widgets import ProfileWidget, GameWidget
from stats_module import pobierz_gry

#kontroler - uruchamia logowanie i jak przejdzie to otwiera główne okno i zamyka login (chyba xd)
class Controller:
    def __init__(self):
        self.login_window = LoginWindow()
        self.login_window.login_success.connect(self.otworz_gra)
        self.otwarte_okna = []

    def start(self):
        self.login_window.show()

    def otworz_profil(self, steamid):
        self.profile_window = ProfileWidget(steamid)
        self.profile_window.show()

    def otworz_gra(self, steamid):
        self.gry = pobierz_gry(0, steamid, 0)
        for n in range(10): #bullshit do wywalenia
            nowe_okno = GameWidget(self.gry[n])
            self.otwarte_okna.append(nowe_okno)
            nowe_okno.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = Controller()
    controller.start()

    sys.exit(app.exec())
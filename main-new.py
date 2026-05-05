import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import Signal, QThread

from login_window import LoginWindow
from widgets import ProfileWidget, GameWidget, MainWindow
from stats_module import pobierz_gry, pobierz_postacie

class PostacieWorker(QThread):
    dane_pobrane = Signal(object)
    def run(self):
        dane = pobierz_postacie()
        self.dane_pobrane.emit(dane)

#kontroler - uruchamia logowanie i jak przejdzie to otwiera główne okno i zamyka login (chyba xd)
class Controller:
    def __init__(self):
        self.login_window = LoginWindow()
        self.login_window.login_success.connect(self.sprawdz_czy_gotowe)
        self.otwarte_okna = []

        self.postacie_dane = {}
        self.postacie_gotowe = False
        self.oczekujace_steamid = None

        self.worker_thread = PostacieWorker()
        self.worker_thread.dane_pobrane.connect(self.zapisz_postacie)
        self.worker_thread.start()

    def sprawdz_czy_gotowe(self, steamid):
        if self.postacie_gotowe:
            self.otworz_main(steamid, self.postacie_dane)
        else:
            print("czekam na dane")
            self.oczekujace_steamid = steamid

    def zapisz_postacie(self, dane):
        self.postacie_dane = dane
        self.postacie_gotowe = True
        if self.oczekujace_steamid is not None:
            self.otworz_main(self.oczekujace_steamid, self.postacie_dane)
            self.oczekujace_steamid = None

    def start(self):
        self.login_window.show()

    def otworz_main(self, steamid, postacie):
        self.main_window = MainWindow(steamid, postacie)
        self.main_window.show()

    # def otworz_profil(self, steamid):
    #     self.profile_window = ProfileWidget(steamid)
    #     self.profile_window.show()
    #
    # def otworz_gra(self, steamid):
    #     self.gry = pobierz_gry(0, steamid, 0)
    #     for n in range(2): #bullshit do wywalenia
    #         danepostaci = self.postcie_dane.get(self.gry[n]['hero_id'])
    #         nowe_okno = GameWidget(self.gry[n],danepostaci)
    #         self.otwarte_okna.append(nowe_okno)
    #         nowe_okno.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = Controller()
    controller.start()

    sys.exit(app.exec())
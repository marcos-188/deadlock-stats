import sys

from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QApplication
from login_window import LoginWindow
from utilities_module import pobierz_postacie_z_api
from widgets import MainWindow


class PostacieWorker(QThread):
    dane_pobrane = Signal(object)
    def run(self):
        dane = pobierz_postacie_z_api()
        heroes_dict = {
            hero["id"]:hero for hero in dane
        }
        self.dane_pobrane.emit(heroes_dict)

#kontroler - uruchamia logowanie i jak przejdzie to otwiera główne okno
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

    def sprawdz_czy_gotowe(self, steamdata):
        if self.postacie_gotowe:
            self.otworz_main(steamdata, self.postacie_dane)
        else:
            print("Czekam na dane postaci")
            self.oczekujace_steamdata = steamdata

    def zapisz_postacie(self, dane):
        self.postacie_dane = dane
        self.postacie_gotowe = True
        if self.oczekujace_steamid is not None:
            self.otworz_main(self.oczekujace_steamid, self.postacie_dane)
            self.oczekujace_steamid = None

    def start(self):
        self.login_window.show()

    def otworz_main(self, steamdata, postacie):
        self.main_window = MainWindow(steamdata, postacie)
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = Controller()
    controller.start()

    sys.exit(app.exec())
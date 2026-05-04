from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import Signal, QEvent
from ui_login import Ui_Form_login
from user_save_module import get_app_dir
from steam_xml import steam_profile_data_finder, steam_id_finder


class LoginWindow(QWidget, Ui_Form_login):
    #login_success = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.steamID64 = None

        self.plik_zapisu = get_app_dir("DeadlockStats") / "zapisany_steam_id.txt"

        if self.plik_zapisu.exists():
            with open(self.plik_zapisu, "r", encoding="utf-8") as f:
                self.steamID64 = int(f.read().strip())
            self.lineEdit_link.setPlaceholderText(f" Znaleziono zapisany link do profilu '{steam_profile_data_finder(self.steamID64)[0]}' (kliknij, aby zmienić)")
            self.lineEdit_link.setReadOnly(True)  # Blokujemy wpisywanie
            self.lineEdit_link.installEventFilter(self)
            self.checkBox_zapisz.setChecked(True)
            self.checkBox_zapisz.setEnabled(False)
        else:
            self.lineEdit_link.setPlaceholderText("Podaj link do profilu Steam")

        self.pushButton_szukaj.clicked.connect(self.szukaj_clicked)

    def szukaj_clicked(self):
        print('1')
        steam_link = self.lineEdit_link.text()
        try:
            if steam_link:
                self.steamID64 = steam_id_finder(steam_link)
                if self.checkBox_zapisz.isChecked():
                    self.plik_zapisu.parent.mkdir(parents=True, exist_ok=True)
                    with open(self.plik_zapisu, "w", encoding="utf-8") as f:
                        f.write(str(self.steamID64))
                    self.lineEdit_link.setPlaceholderText(f" Znaleziono zapisany link do profilu '{steam_profile_data_finder(self.steamID64)[0]}' (kliknij, aby zmienić)")
                    self.checkBox_zapisz.setEnabled(False)
                    self.lineEdit_link.clear()
                elif self.plik_zapisu.exists():
                    with open(self.plik_zapisu, "r", encoding="utf-8") as f:
                        self.steamID64 = int(f.read().strip())
                else:
                    QMessageBox.warning(self, "Błąd", "Proszę podać link do profilu Steam.")
                    return
        except Exception as e:
            QMessageBox.warning(self, "Błąd", e)
            self.lineEdit_link.clear()


    #jeżeli jest już zapisane steam id i zablokuje sie przez to wpisywanie to program na kliknięcie pola wprowadzania linku wyświetla komunikat że już znaleziono zapisany profil
    def eventFilter(self, source, event):
        if source is self.lineEdit_link and event.type() == QEvent.MouseButtonPress:
            if self.lineEdit_link.isReadOnly():
                odpowiedz = QMessageBox.question(
                    self,
                    "Zapisane konto",
                    f"Program znalazł zapisany wcześniej profil steam.\nCzy chcesz usunąć zapis i wprowadzić nowy link?",
                    QMessageBox.Yes | QMessageBox.No
                )

                if odpowiedz == QMessageBox.Yes:
                    self.lineEdit_link.setReadOnly(False)
                    self.checkBox_zapisz.setEnabled(True)
                    self.lineEdit_link.clear()
                    self.lineEdit_link.setPlaceholderText("Link do profilu Steam")

                    if self.plik_zapisu.exists():
                        self.plik_zapisu.unlink()

                return True  # Informujemy system, że obsłużyliśmy to kliknięcie

        return super().eventFilter(source, event)
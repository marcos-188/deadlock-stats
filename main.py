import os
from pathlib import Path

from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QComboBox,
    QPushButton, QLineEdit, QMainWindow, QMessageBox, QHBoxLayout, QCheckBox)

from stats_module import steam_id_find_gui, pobierz_gry, wypisz_statystyki


def get_app_dir(nazwa_programu):
    katalog_domowy = Path.home()
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / nazwa_programu
    else:
        return katalog_domowy / "AppData" / "Roaming" / nazwa_programu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pobrane_gry = None
        self.setWindowTitle("Deadlock Stats")

        self.plik_zapisu = get_app_dir("DeadlockStats") / "zapisany_steam_id.txt"

        #główne okno
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        label_1 = QLabel("Wprowadzanie danych")
        label_1.setAlignment(Qt.AlignCenter)

        #container z linkiem i zapisywaniem steamID
        containter_link = QWidget()
        layout_link = QVBoxLayout(containter_link)
        self.line_edit_link = QLineEdit()
        self.checkbox_zapisz = QCheckBox("Zapisz profil")

        if self.plik_zapisu.exists():
            self.line_edit_link.setPlaceholderText("Znaleziono zapisany link (kliknij, aby zmienić)")
            self.line_edit_link.setReadOnly(True)  # Blokujemy wpisywanie
            self.line_edit_link.installEventFilter(self)
            self.checkbox_zapisz.setChecked(True)
            self.checkbox_zapisz.setEnabled(False)
        else:
            self.line_edit_link.setPlaceholderText("Podaj link do profilu Steam")

        #container z combo boxami
        containter_combo_boxy = QWidget()
        layout_combo_boxy = QHBoxLayout(containter_combo_boxy)

        # container z combo box ile
        containter_combo_ile = QWidget()
        layout_combo_ile = QVBoxLayout(containter_combo_ile)

        label_2 = QLabel("Ile gier")
        label_2.setAlignment(Qt.AlignCenter)

        self.combo_box_ile_gier = QComboBox()
        self.combo_box_ile_gier.addItem("Wszystkie",0)
        self.combo_box_ile_gier.addItem("5",5)
        self.combo_box_ile_gier.addItem("10",10)
        self.combo_box_ile_gier.addItem("25",25)
        self.combo_box_ile_gier.addItem("50",50)
        self.combo_box_ile_gier.addItem("100",100)

        # container z combo box brawl
        containter_combo_brawl = QWidget()
        layout_combo_brawl = QVBoxLayout(containter_combo_brawl)
        label_3 = QLabel("Jakie tryby gier uwzględniać")
        label_3.setAlignment(Qt.AlignCenter)

        self.combo_box_czy_brawl = QComboBox()
        self.combo_box_czy_brawl.addItems(["Tylko zwykłe gry", "Wszystkie gry", "Tylko gry Brawl"])

        container_buttony = QWidget()
        layout_buttony = QHBoxLayout(container_buttony)

        self.button_szukaj = QPushButton("Pobierz")
        self.button_szukaj.clicked.connect(self.szukaj_clicked)

        self.button_statystyki = QPushButton("Statystyki")
        self.button_statystyki.clicked.connect(self.statystyki_clicked)
        self.button_statystyki.setEnabled(False)

        layout.addWidget(label_1)
        layout.addWidget(containter_link)
        layout.addWidget(self.line_edit_link)
        layout.addWidget(containter_combo_boxy)
        layout.addWidget(container_buttony)

        layout_link.addWidget(self.line_edit_link)
        layout_link.addWidget(self.checkbox_zapisz)

        layout_combo_boxy.addWidget(containter_combo_ile)
        layout_combo_boxy.addWidget(containter_combo_brawl)

        layout_combo_ile.addWidget(label_2)
        layout_combo_ile.addWidget(self.combo_box_ile_gier)

        layout_combo_brawl.addWidget(label_3)
        layout_combo_brawl.addWidget(self.combo_box_czy_brawl)

        layout_buttony.addWidget(self.button_szukaj)
        layout_buttony.addWidget(self.button_statystyki)

    def szukaj_clicked(self):
        steam_link = self.line_edit_link.text()
        ile_gier = int(self.combo_box_ile_gier.currentData())
        czy_brawl = self.combo_box_czy_brawl.currentIndex()

        try:
            steam_id = ""#steam_id_find_gui(steam_link)
            if steam_link:
                steam_id = steam_id_find_gui(steam_link)

                if self.checkbox_zapisz.isChecked():
                    self.plik_zapisu.parent.mkdir(parents=True, exist_ok=True)
                    with open(self.plik_zapisu, "w", encoding="utf-8") as f:
                        f.write(str(steam_id))
                    self.line_edit_link.setPlaceholderText("Znaleziono zapisany link")
                    self.checkbox_zapisz.setEnabled(False)
                    self.line_edit_link.clear()
            elif self.plik_zapisu.exists():
                with open(self.plik_zapisu, "r", encoding="utf-8") as f:
                    steam_id = int(f.read().strip())
            else:
                QMessageBox.warning(self, "Błąd", "Proszę podać link do profilu Steam.")
                return

            self.pobrane_gry = pobierz_gry(ile_gier,steam_id, czy_brawl)
            if len(self.pobrane_gry) == 0:
                QMessageBox.warning(self, "Błąd", "Nie rozegrano jeszcze żadnej gry lub podano złe konto")
                self.line_edit_link.clear()
            else:
                self.button_statystyki.setEnabled(True)
                print(steam_id)
                QMessageBox.information(self,"Sukces",f"Pobrano {len(self.pobrane_gry)} gier.")

        except ValueError as e:
            error_message = str(e)
            QMessageBox.warning(self, "Błąd", error_message)

            self.line_edit_link.clear()

    def statystyki_clicked(self):
        pobrane_satatystyki = wypisz_statystyki(self.pobrane_gry)
        QMessageBox.information(self, "Statystyki", pobrane_satatystyki)

    def eventFilter(self, source, event):
        # Sprawdzamy, czy zdarzenie to kliknięcie w nasze pole linku
        if source is self.line_edit_link and event.type() == QEvent.MouseButtonPress:
            # Reagujemy tylko, jeśli pole jest zablokowane (jest zapisany link)
            if self.line_edit_link.isReadOnly():
                odpowiedz = QMessageBox.question(
                    self,
                    "Zapisane konto",
                    "Masz już przypisane konto do tego programu.\nCzy chcesz usunąć zapis i wprowadzić nowy link?",
                    QMessageBox.Yes | QMessageBox.No
                )

                if odpowiedz == QMessageBox.Yes:
                    # Odblokowujemy pole
                    self.line_edit_link.setReadOnly(False)
                    self.checkbox_zapisz.setEnabled(True)
                    self.line_edit_link.clear()
                    self.line_edit_link.setPlaceholderText("Link do profilu Steam")
                    # Usuwamy stary plik z dysku
                    if self.plik_zapisu.exists():
                        self.plik_zapisu.unlink()

                return True  # Informujemy system, że obsłużyliśmy to kliknięcie

        return super().eventFilter(source, event)


app = QApplication()
window = MainWindow()
window.setFixedSize(500, 350)
window.show()
app.exec()
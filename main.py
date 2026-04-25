import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,QMainWindow, QLabel, QWidget, QVBoxLayout, QProgressBar, QComboBox,
    QGridLayout,QPushButton, QLineEdit,QTextEdit,QMainWindow,QSlider, QListWidget,QRadioButton,
    QMessageBox)
from stats_module import steam_id_find_gui,pobierz_gry

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Deadlock Stats")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label_1 = QLabel("Wprowadzanie danych")
        label_1.setAlignment(Qt.AlignCenter)

        self.line_edit_link = QLineEdit(placeholderText="Link do profilu Steam")

        label_2 = QLabel("Ile gier")
        label_2.setAlignment(Qt.AlignCenter)

        self.combo_box_ile_gier = QComboBox()
        self.combo_box_ile_gier.addItem("Wszystkie",0)
        self.combo_box_ile_gier.addItem("5",5)
        self.combo_box_ile_gier.addItem("10",10)
        self.combo_box_ile_gier.addItem("25",25)
        self.combo_box_ile_gier.addItem("50",50)
        self.combo_box_ile_gier.addItem("100",100)



        self.button_szukaj = QPushButton("Szukaj")
        self.button_szukaj.clicked.connect(self.szukaj_clicked)

        self.combo_box_czy_brawl = QComboBox()
        self.combo_box_czy_brawl.addItems(["Tylko zwykłe gry", "Wszystkie gry", "Tylko gry Brawl"])

        layout.addWidget(label_1)
        layout.addWidget(self.line_edit_link)
        layout.addWidget(label_2)
        layout.addWidget(self.combo_box_ile_gier)
        layout.addWidget(self.combo_box_czy_brawl)
        layout.addWidget(self.button_szukaj)

    def szukaj_clicked(self):
        steam_link = self.line_edit_link.text()
        ile_gier = int(self.combo_box_ile_gier.currentData())
        czy_brawl = self.combo_box_czy_brawl.currentIndex()

        try:
            steam_id = steam_id_find_gui(steam_link)
            pobrane_gry = pobierz_gry(ile_gier,steam_id, czy_brawl)
            print(len(pobrane_gry))
            #print(f"znaleziono - {steam_id}")
            #print(ile_gier)
            #print(czy_brawl)
        except ValueError as e:
            error_message = str(e)
            QMessageBox.warning(self, "Błąd", error_message)

            self.line_edit_link.clear()









app = QApplication()
window = MainWindow()
window.show()
app.exec()
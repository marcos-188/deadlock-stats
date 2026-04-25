import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,QMainWindow, QLabel, QWidget, QVBoxLayout, QProgressBar, QComboBox,
    QGridLayout,QPushButton, QLineEdit,QTextEdit,QMainWindow,QSlider, QListWidget,QRadioButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Deadlock Stats")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label_1 = QLabel("Wprowadzanie danych")
        label_1.setAlignment(Qt.AlignCenter)

        line_edit = QLineEdit("Link do profilu Steam")

        label_2 = QLabel("Ile gier")
        label_2.setAlignment(Qt.AlignCenter)

        combo_box_ile_gier = QComboBox()
        combo_box_ile_gier.addItems(["5","10","25","50","100","Wszystkie"])


        button_szukaj = QPushButton("Szukaj")

        combo_box_czy_brawl = QComboBox()
        combo_box_czy_brawl.addItems(["Tylko zwykłe gry", "Wszystkie gry", "Tylko gry Brawl"])

        layout.addWidget(label_1)
        layout.addWidget(line_edit)
        layout.addWidget(label_2)
        layout.addWidget(combo_box_ile_gier)
        layout.addWidget(combo_box_czy_brawl)
        layout.addWidget(button_szukaj)



app = QApplication()
window = MainWindow()
window.show()
app.exec()
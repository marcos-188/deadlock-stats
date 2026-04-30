import sys
import os
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QFile
from PySide6.QtWidgets import (QApplication)
from PySide6.QtUiTools import QUiLoader

app = QApplication()
loader = QUiLoader()
window = loader.load("qt-designer/profil-gui.ui")

def get_app_dir(nazwa_programu):
    katalog_domowy = Path.home()
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / nazwa_programu
    else:
        return katalog_domowy / "AppData" / "Roaming" / nazwa_programu

def na_klikniecie_przycisku():
    plik_zapisu = get_app_dir("DeadlockStats") / "zapisany_steam_id.txt"
    print("Przycisk został kliknięty!")
    with open(plik_zapisu, "r", encoding="utf-8") as f:
        steam_id64 = int(f.read().strip()) + 76561197960265728
    window.label.setText(str(steam_id64))

window.pushButton.clicked.connect(na_klikniecie_przycisku)

window.show()
app.exec()

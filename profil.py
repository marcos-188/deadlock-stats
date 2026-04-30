import sys
import os
import urllib.request
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QFile
from PySide6.QtWidgets import (QApplication)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from steam_xml import steam_profile_data_finder

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


def load_image_from_url(url, label):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
    except Exception as e:
        print(f"Nie udało się załadować obrazka: {e}")
        label.setText("Błąd ładowania obrazka")

def na_klikniecie_przycisku():
    plik_zapisu = get_app_dir("DeadlockStats") / "zapisany_steam_id.txt"
    print("Przycisk został kliknięty!")
    with open(plik_zapisu, "r", encoding="utf-8") as f:
        steamid64 = int(f.read().strip())
    dane = steam_profile_data_finder(steamid64)
    window.label.setText(str(dane[0]))
    load_image_from_url(dane[1], window.label_obrazek)

window.pushButton.clicked.connect(na_klikniecie_przycisku)

window.show()
app.exec()

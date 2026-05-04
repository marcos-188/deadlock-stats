import sys
import os
from pathlib import Path
import urllib.request
from PySide6.QtGui import QPixmap

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
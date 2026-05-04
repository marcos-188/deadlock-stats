import sys
import os
from pathlib import Path

def get_app_dir(nazwa_programu):
    katalog_domowy = Path.home()
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / nazwa_programu
    else:
        return katalog_domowy / "AppData" / "Roaming" / nazwa_programu
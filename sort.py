import os
import shutil
from pathlib import Path

desktop_path = Path.home()/ "Рабочий стол"

folders = {
    "json_files": [".json"],
    "deb_installers": [".deb"],
    "Pictures": [".jpeg", ".jpg", ".png"]
}

for folder_name in folders.keys():
    (desktop_path / folder_name).mkdir(exist_ok=True)

for item in desktop_path.iterdir():
    if item.is_file():
        ext = item.suffix.lower()

        for folder_name, extensions in folder.items():
            if ext in extensions:
              
              shutil.move(str(item), str(desktop_path / folder_name / item.name))
              print("{item.name} to {folder_name}")
              break 

print("Done!")
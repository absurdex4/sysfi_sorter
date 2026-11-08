import os
import shutil
from pathlib import Path

desktop_path = Path.home()/ "Рабочий стол"

folders = {
    "json_files": [".json"],
    "deb_installers": [".deb"],
    "pics": [".jpeg", ".jpg", ".png"]
}

for folder_name in folders.keys():
    (desktop_path / folder_name).mkdir(exist_ok=True)

for item in desktop_path.iterdir():
    if item.is_file():
        ext = item.suffix.lower()

        for folder_name, extensions in folders.items():
            if ext in extensions:
                target_path = desktop_path / folder_name / item.name
                try:
                    shutil.move(str(item), str(target_path))
                    print(f"Success! {item.name} > {folder_name}")
                except Exception as e:
                    print(f"Smth isn`t right here...")
                break 

print("Done!")
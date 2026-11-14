import shutil
from pathlib import Path

home = Path.home()
sources = []
for name in ["Desktop", "Рабочий стол", "Downloads", "Загрузки"]:
    p = home / name 
    if p.exists() and p.is_dir():
        sources.append(p)

if not sources:
    print("Not found")
    exit()

targets = {
    "Pictures": {
        "path": home / "Pictures",
        "extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"]
    },
    "Service": {
        "path": home / "Service",
        "extensions": [
            #установщики
            ".deb", ".rpm", ".appimage", ".AppImage", ".exe", ".msi",
            #архивы 
            ".zip", ".rar", ".7z", ".tar", ".gz", ".tar.gz", ".tgz", ".bz2", ".xz",
            #прочее
            ".json", ".iso"
        ]
    }
}

for info in targets.values():
    info["path"].mkdir(exist_ok=True)

for source in sources:
    for item in source.iterdir():
        if not item.is_file():
            continue

        target_dir, category = find_target(item.name.lower())
        if target_dir is None:
            continue

        try:
            dst = safe_move(item, target_dir)
            print(f"{item.name} > {category}")
        except Exception as e:
            print(f"Smth isn`t right here...")

print("Done!")
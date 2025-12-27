import json
import os
from pathlib import Path

INPUT_FILE = "input.json"
OUTPUT_DIR = "output"

# читаем JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

if "files" not in data or not isinstance(data["files"], list):
    raise ValueError("Ожидался массив 'files' в JSON")

# создаём output/
os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in data["files"]:
    # пропускаем telegram id и любые служебные записи
    if "name" not in file or "content" not in file:
        continue

    file_path = Path(OUTPUT_DIR) / file["name"]
    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = file["content"]

    # если content — объект, сериализуем в JSON
    if isinstance(content, (dict, list)):
        content = json.dumps(content, indent=2, ensure_ascii=False)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ created: {file['name']}")

print("\nГотово. Astro-проект собран в папке output/")
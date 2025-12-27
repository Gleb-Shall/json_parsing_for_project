import fs from "fs";
import path from "path";

const INPUT_FILE = "./input.json";
const OUTPUT_DIR = "./output";

const raw = fs.readFileSync(INPUT_FILE, "utf-8");
const data = JSON.parse(raw);

if (!Array.isArray(data.files)) {
  throw new Error("Ожидался массив files");
}

fs.mkdirSync(OUTPUT_DIR, { recursive: true });

for (const file of data.files) {
  if (!file.name || file.content === undefined) continue;

  const filePath = path.join(OUTPUT_DIR, file.name);
  fs.mkdirSync(path.dirname(filePath), { recursive: true });

  const content =
    typeof file.content === "object"
      ? JSON.stringify(file.content, null, 2)
      : file.content;

  fs.writeFileSync(filePath, content, "utf-8");
  console.log("✔ created:", file.name);
}

console.log("Готово");
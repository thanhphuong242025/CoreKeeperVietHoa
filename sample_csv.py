import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"

samples = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='\t')
    for idx, row in enumerate(reader):
        if idx > 0 and idx % 75 == 0:
            samples.append((idx, row[0], row[2], row[3] if len(row) > 3 else ""))

for idx, key, eng, viet in samples:
    print(f"[{idx}] {key}\n  ENG: {eng}\n  VIE: {viet}\n")

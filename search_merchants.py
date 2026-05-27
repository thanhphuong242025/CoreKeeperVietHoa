import csv

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='\t')
    rows = list(reader)

with open("merchant_analysis.txt", "w", encoding="utf-8") as out:
    for idx, row in enumerate(rows):
        if len(row) > 0:
            key = row[0]
            val = row[3] if len(row) > 3 else ""
            if "merchant" in key.lower() or "thương nhân" in val.lower():
                out.write(f"Row {idx+1} | Key: {key}\n")
                out.write(f"  Desc: {repr(row[2]) if len(row) > 2 else ''}\n")
                out.write(f"  Thai: {repr(val)}\n\n")

print("Done")

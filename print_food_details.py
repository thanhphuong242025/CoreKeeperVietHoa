import csv

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='\t')
    rows = list(reader)

targets = ["foodFormat", "rareItemFormat", "Rarity/Rare", "Rarity/RareFemale", "Rarity/RareMale"]
with open("food_details.txt", "w", encoding="utf-8") as out:
    for row in rows:
        if len(row) > 0 and row[0] in targets:
            out.write(f"Key: {row[0]}\n")
            out.write(f"  Desc (EN): {repr(row[2]) if len(row) > 2 else ''}\n")
            out.write(f"  Thai (VN): {repr(row[3]) if len(row) > 3 else ''}\n\n")

print("Done")

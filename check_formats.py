import csv

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='\t')
    rows = list(reader)

with open("format_patterns.txt", "w", encoding="utf-8") as out:
    for idx, row in enumerate(rows):
        if len(row) > 3:
            val = row[3]
            if "{" in val and "}" in val:
                out.write(f"Row {idx+1} | Key: {row[0]}\n")
                out.write(f"  Thai: {repr(val)}\n\n")

print("Done")

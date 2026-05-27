import csv

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"

# Count total rows, empty rows in the 4th column, and matching English rows
total = 0
empty = 0
untranslated_same = 0

with open(csv_path, "r", encoding="utf-8") as f:
    # Read as TSV
    reader = csv.reader(f, delimiter='\t')
    for idx, row in enumerate(reader):
        if idx == 0:
            print("Header:", row)
            continue
        total += 1
        if len(row) <= 3 or not row[3].strip():
            empty += 1
        elif len(row) > 3 and len(row) > 2:
            # Check if translation is same as ID (which is the English source)
            # Row structure: Key, Type, Id (English), Thai (Vietnamese)
            eng = row[2]
            viet = row[3]
            if eng.strip() == viet.strip() and len(eng.strip()) > 3:
                # Exclude formatting keys or variables like [0], {0}, etc.
                if not eng.startswith("[") and not eng.startswith("{") and not eng.isdigit():
                    untranslated_same += 1

print(f"Total entries: {total}")
print(f"Empty entries in Vietnamese column: {empty}")
print(f"Entries where Vietnamese is identical to English: {untranslated_same}")

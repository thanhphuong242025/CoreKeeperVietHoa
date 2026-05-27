import gzip
import os

csv_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.csv"
dat_path = r"d:\ProgramFiles\Steam\steamapps\common\Core Keeper\localization\Localization.dat"

if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found.")
    exit(1)

with open(csv_path, "r", encoding="utf-8") as f:
    csv_text = f.read()

# 1. Compress with gzip
compressed = gzip.compress(csv_text.encode('utf-8'))

# 2. XOR encrypt with key "Keeper"
key = b"Keeper"
encrypted = bytearray(compressed)
for i in range(len(encrypted)):
    encrypted[i] ^= key[i % len(key)]

with open(dat_path, "wb") as f:
    f.write(encrypted)

print(f"Successfully encrypted {csv_path} into {dat_path}")

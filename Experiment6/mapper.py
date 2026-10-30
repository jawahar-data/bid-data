import re
from pathlib import Path
from collections import defaultdict

# Input text file
data_path = Path(__file__).resolve().with_name("data.txt")
with data_path.open("r", encoding="utf-8") as f:
    lines = f.readlines()

# Mapper
mapper_output = []
for line in lines:
    line = line.strip().lower()
    words = re.split(r"\s+", line)
    for word in words:
        if word:
            mapper_output.append((word, 1))

print("=== Mapper Output ===")
for word, count in mapper_output:
    print(f"{word}\t{count}")

# Shuffle/Sort
sorted_output = sorted(mapper_output, key=lambda x: x[0])

print("\n=== Sorted Output ===")
for word, count in sorted_output:
    print(f"{word}\t{count}")

# Reducer
reducer_output = defaultdict(int)
for word, count in sorted_output:
    reducer_output[word] += count

print("\n=== Reducer Output ===")
for word, count in reducer_output.items():
    print(f"{word}\t{count}")

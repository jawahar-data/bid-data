import pickle
from pathlib import Path

import pandas as pd


script_dir = Path(__file__).resolve().parent
data = pd.read_csv(script_dir / "data.csv")

# Slicing data
slice1 = data.iloc[0:399, :]
slice2 = data.iloc[400:800, :]
slice3 = data.iloc[801:1200, :]
slice4 = data.iloc[1201:, :]


def mapper(data):
    mapped = []
    for _, row in data.iterrows():
        mapped.append((row["quality"], row["volatile acidity"]))
    return mapped


map1 = mapper(slice1)
map2 = mapper(slice2)
map3 = mapper(slice3)
map4 = mapper(slice4)

shuffled = {}
for mapped_slice in (map1, map2, map3, map4):
    for quality, volatile_acidity in mapped_slice:
        shuffled.setdefault(quality, []).append(volatile_acidity)

with (script_dir / "shuffled.pkl").open("wb") as file:
    pickle.dump(shuffled, file)

print("Data has been mapped.")


# Reducer
def reduce(shuffled_dict):
    return {
        quality: sum(volatile_acidity_values) / len(volatile_acidity_values)
        for quality, volatile_acidity_values in shuffled_dict.items()
        if volatile_acidity_values
    }


final = reduce(shuffled)
print("Average volatile acidity in different classes of wine:")
for quality, average in final.items():
    print(quality, ":", average)
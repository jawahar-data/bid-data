import pandas as pd
import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "data.csv")
data = pd.read_csv(csv_path)

slice1 = data.iloc[0:4,:]
slice2 = data.iloc[4:8,:]

def mapper(data_slice):
    mapped = []
    for index,row in data_slice.iterrows():
        mapped.append((row['quality'],row['volatile acidity']))
    return mapped

map1 = mapper(slice1)
map2 = mapper(slice2)

shuffled = { 3.0:[], 4.0:[], 5.0:[], 6.0:[], 7.0:[], 8.0:[] }

for i in [map1, map2]:
    for j in i:
        if j[0] in shuffled:
            shuffled[j[0]].append(j[1])

pkl_path = os.path.join(script_dir, 'shuffled.pkl')
with open(pkl_path, 'wb') as file:
    pickle.dump(shuffled, file)

print("Data has been mapped and saved to shuffled.pkl.")

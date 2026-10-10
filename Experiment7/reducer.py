import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(script_dir, 'shuffled.pkl')
with open(pkl_path,'rb') as file:
    shuffled = pickle.load(file)

def reduce(shuffled_dict):
    reduced = {}
    for i in shuffled_dict:
        if len(shuffled_dict[i]) > 0:
            reduced[i] = sum(shuffled_dict[i])/len(shuffled_dict[i])
    return reduced

final = reduce(shuffled)
print("Average volatile acidity in different classes of wine: ")
for k, v in final.items():
    print(k,':', v)

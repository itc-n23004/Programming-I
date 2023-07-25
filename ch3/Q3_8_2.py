import pickle

with open("test1.pkl", "rb") as f:
    x = pickle.load(f)
    print(x)

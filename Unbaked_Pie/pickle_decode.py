import pickle

f = open("download.dat", "rb")

data = pickle.load(f)

data.sort()
for i in data:
        print(i)
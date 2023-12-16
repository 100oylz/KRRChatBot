from package.io import load_csv

data=load_csv('data/ownthink_v2.csv')
print(data.keys())
print((len(data)))

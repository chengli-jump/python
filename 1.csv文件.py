import csv

csv_file = "data/home/aistudio/data/data20465/cities.csv"

f = open(csv_file)
data = csv.reader(f)
for line in data:
    print(line)

import pandas as pd 
df = pd.read_csv(csv_file)
print(df)

print(pd.read_csv(csv_file, index_col=0))

diabetes = pd.read_csv("data/home/aistudio/data/data20465/diabetes.csv")
print(diabetes)
print(diabetes.head(3))

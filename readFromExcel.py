import pandas as pd
import xlrd
x=pd.read_csv("test_dataset/test_courses.csv",header=None)
print(x)

print("\n\n\n")
list_of_csv = [list(row) for row in x.values]
print(list_of_csv)


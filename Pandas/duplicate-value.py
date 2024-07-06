import pandas as pd 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
print(data)
print(data.duplicated().sum())
print(data.drop_duplicates())# used to remove duplicate 
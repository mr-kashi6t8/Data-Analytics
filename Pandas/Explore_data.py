import pandas as pd 

data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
# print(data)
# print(data.head(10))
# print(data.tail(10))# for big data we can access these 
# print(data.info())# we can get all info about data 
# print(data.describe())
print(data.isnull().sum())
import pandas as pd 
import numpy as np 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
# print(data)
# print(data.isnull().sum())
# print(data.dropna())# used to drop all bull value 
# print(data.replace(np.nan,"Hi"))# its used to replace some values with  all the null
# data["Unnamed: 0"] = data["Unnamed: 0"].replace(np.nan,"2000") # Hence used to replace at specific coloumn

print(data)

# print(data["Unnamed: 5"].mean())# since he have to check the mean value of data and fill in it so the mean of data was same 
# print(data.fillna(method= "bfill")) # we use f fill and b fill to fill the null values so no change occur on it 


import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
# Sample Data 
# brands = ["OnePlus","Iphone","Samsung","Nokia"]
# x = [20,80,60,40]
# c = ["Red","Silver","Blue","Yellow"]
# ex = [0,0.1,0,0]
# plt.pie(x ,labels=brands,colors=c,explode=ex,shadow= True,autopct="%.2f",startangle=90)
# plt.show()

# get data from excel 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
grouped_data=df.groupby("Project Name")["Progress"].sum()
# plt.pie(df["Progress"],labels=df["Project Name"])
# c = np.random.randint(10,100,50)

plt.pie(grouped_data.values,labels=grouped_data.index,shadow= True,autopct="%.2f",startangle=90)
plt.show()
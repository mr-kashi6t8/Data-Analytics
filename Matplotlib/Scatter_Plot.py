import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


# x = np.random.randint(1,10,50)
# y = np.random.randint(10,100,50)
# v = np.random.randint(10,100,50)
# # print(x)
# # print(y)
# plt.scatter(x,y,marker="*",cmap = "hot", c=v)
# plt.colorbar()
# plt.show()


# Import from any data 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
color = np.random.randint(10,100,18)
grouped_data=df.groupby("Days Required")["Progress"].sum()
print(grouped_data)
plt.scatter(grouped_data.index,grouped_data.values,marker="*" ,cmap="hot",c= color)

# plt.scatter(df["Days Required"],df["Progress"],marker="*" ,cmap="hot",c= color)
plt.colorbar()
plt.show()
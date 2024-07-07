import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

# x = ["Day 1","Day 2","Day 3","Day 4","Day 5",]
# y=[10,23,45,23,45]

# plt.step(x,y,where="mid",marker="o")
# plt.legend()
# plt.show()
# If we plot it on Data Set
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
grouped_by=df.groupby("Project Name") ["Progress"].sum()
print(grouped_by)
plt.step(grouped_by.index.unique(),grouped_by.values)
plt.show()
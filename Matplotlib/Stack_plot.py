import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
# days = [1,2,3,4,5,6,7]
# NOP1=[10,23,45,23,45,2,45]
# NOP2=[1,23,4,3,4,2,45]
# NOP3=[19,23,46,34,4,2,45]
# plt.stackplot(days,NOP1,NOP2,NOP3,labels=["Week1","Week2","Week3"])
# plt.legend()
# plt.show()


# For Outer data 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
grouped_by=df.groupby("Project Name") ["Progress"].sum()
print(grouped_by)
plt.stackplot(grouped_by.index,grouped_by.values)
plt.show()
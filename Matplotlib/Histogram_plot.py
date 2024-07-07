import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
# x = [12,17,13,15,18,20,30,40,50,78,90,30,20,45,80,30]
# plt.hist(x, bins=15,edgecolor="black",color="pink")
# plt.show()

# This is we take data from data set 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
plt.hist(df["Days Required"],bins=20)
plt.show()
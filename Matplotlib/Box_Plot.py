import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# This is for random Data Values 
# l = [1,3,4,7,12,2,8,9,24]
# l2=[2,3,4,5,6,78,9,9]
# plot_values=[l,l2]
# plt.boxplot(plot_values)
# plt.show()

# This is we fetch data from excel file 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
# print(df)
plt.boxplot(df["Progress"])
plt.show()
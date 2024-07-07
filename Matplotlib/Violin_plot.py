import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 



# a = [12,34,56,23,45,23,45,67,87,80,82,81,85,78,79,80,98]
# plt.violinplot(a,showmedians=True)
# plt.show()


# use it on data set 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)

plt.violinplot(df["Days Required"],showmedians=True)
plt.show()
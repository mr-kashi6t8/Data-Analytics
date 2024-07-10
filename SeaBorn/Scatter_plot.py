import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns
# Its placed between two numerical values 

# data = sns.load_dataset("tips")
# print(data)
# sns.scatterplot(data,x="total_bill",y="tip",hue="sex",size="size",palette="spring")
# plt.show()
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
sns.scatterplot(data,x="Days Required",y="Progress",hue="Project Name")
# plt.figure(figsize=0.2)
plt.legend(bbox_to_anchor=(0.2,0,1.2,1))#(x,y,width,height)
plt.show()
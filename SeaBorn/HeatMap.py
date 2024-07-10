import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
# this is the data we take from seaborn 

# data = sns.load_dataset("tips")
# print(data)
# gp = data.groupby("day").agg({"tip":"mean"})
# print(gp)
# sns.heatmap(gp)
# plt.show()

# hene we have to take value from data set 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
gp = data.groupby("Project Name").agg({"Progress":"mean"})
print(gp)
sns.heatmap(gp)
plt.show()
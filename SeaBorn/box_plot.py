import matplotlib.pylab as plt
import pandas as pd 
import seaborn as sns
data = sns.load_dataset("tips")
print(data)
# gp = data.groupby("day").agg({"tip":"mean"})
# print(gp)
sns.boxplot(data,x="day",y="tip",orient="vertical")
plt.show()
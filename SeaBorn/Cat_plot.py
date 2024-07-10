import matplotlib.pylab as plt
import pandas as pd 
import seaborn as sns
data = sns.load_dataset("tips")
print(data)
# gp = data.groupby("day").agg({"tip":"mean"})
# print(gp)
sns.catplot(data,x="day", y="tip",hue="sex",kind="bar")
sns.set_style(style="ticks" )
plt.show()
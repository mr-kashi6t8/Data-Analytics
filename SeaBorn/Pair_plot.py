import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 
data = sns.load_dataset("iris")
print(data)
# gp = data.groupby("day").agg({"tip":"mean"})
# print(gp)
sns.pairplot(data,hue="species")
plt.show()
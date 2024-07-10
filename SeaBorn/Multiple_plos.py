import matplotlib.pylab as plt
import pandas as pd 
import seaborn as sns
data = sns.load_dataset("tips")
print(data)
a = sns.FacetGrid(data,col="time",hue="sex")
a.map(sns.barplot,"day","tip")
plt.show()
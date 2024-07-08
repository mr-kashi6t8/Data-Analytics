import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 
data = sns.load_dataset("tips")
print(data)
sns.barplot(data= data ,x="day",y="tip",hue="sex",palette="spring",errorbar=("ci",0))
plt.plot()
plt.show()
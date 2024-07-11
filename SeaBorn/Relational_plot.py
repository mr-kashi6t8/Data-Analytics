import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
data = sns.load_dataset("tips")
# print(data)
sns.relplot(data,x="tip",y="total_bill",hue="sex",col="day",size="smoker")
plt.show()
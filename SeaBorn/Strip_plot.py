import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns
data = sns.load_dataset("tips")
print(data)
sns.stripplot(data,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()
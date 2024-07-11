import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pnd 
data = sns.load_dataset("tips")
print(data) 
# sns.histplot(data,x="total_bill")
sns.kdeplot(data,x="total_bill",hue="day",multiple="stack")
plt.show()

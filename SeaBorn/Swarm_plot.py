import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pnd 
data = sns.load_dataset("tips")
print(data)
# In swarm plot data don not overlap 
sns.swarmplot(data,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()
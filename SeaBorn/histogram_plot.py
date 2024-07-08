import matplotlib.pyplot as plt 
import seaborn as sns 
# to count the frequency of data 

# data = sns.load_dataset("tips")
# print(data)
data = sns.load_dataset("titanic")
print(data)
sns.histplot(data=data,x="age",hue="who",kde=True,discrete=True)
plt.title("Age Determination On The Basis Of Who",fontsize=15)
plt.xlabel("Age",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()
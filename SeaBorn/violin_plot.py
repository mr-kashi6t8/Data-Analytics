import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 
# data = sns.load_dataset("tips")
# print(data)
# sns.violinplot(data,x="tip")
# plt.show()

# take data from data set 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
sns.violinplot(df,x="Progress")
plt.show()
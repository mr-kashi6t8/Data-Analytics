import matplotlib.pylab as plt
import pandas as pd 
import seaborn as sns
# data = sns.load_dataset("tips")
# print(data)
# # gp = data.groupby("day").agg({"tip":"mean"})
# # print(gp)
# sns.countplot(data,x="day")
# plt.show()


# Hence we take data from Data set 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
# gp=data.groupby("Project Name")["Progress"].sum().reset_index()
# print(gp)
sns.countplot(df,x="Project Name",palette="viridis",hue="Progress")
plt.xlabel("Project Name",fontsize=10)
# plt.ylabel("Progress",fontsize=10)
plt.legend()
plt.xticks(rotation=45)
plt.show()
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

# if we make data frame
# data = {
#     "Days":[1,2,3,4,5],
#     "NOP":[25,67,89,30,45]
# }
# df = pd.DataFrame(data)
# print(df)
# sns.lineplot(data=data,x="Days",y="NOP")
# plt.show()

# if we access data frm ecxel
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
# This is for grouped data 
# grouped_data = df.groupby(["Project Name"])["Progress"].sum().reset_index()
# print(grouped_data)
# sns.lineplot(data= grouped_data , x="Project Name",y="Progress")
# plt.show()
# This is for ungrouped data
sns.lineplot(data= data , x="Task Name",y="Days Required",hue="Project Name",)
plt.legend(loc="upper right",borderpad=-6)
plt.show()
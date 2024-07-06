import matplotlib.pyplot as plt
import pandas as pd 
# *************************This  is simple **********************
# x = [ 20,40,50,70]
# y = ["Part 1","Part 2","Part 3","Part 4"]
# colors = ["Red","Green","Yellow","Orange"]
# plt.bar(y,x,color=colors,)
# plt.xlabel("Parts Of Harry Potter")
# plt.ylabel("Popularity")
# plt.title("POpularity Of Different Parts Of Harry Potter ",fontsize=20)
# plt.show()
# ************** So if We wants to access data from Data frames 
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
grouped_by=df.groupby("Project Name") ["Progress"].sum()
print(grouped_by)
plt.bar(grouped_by.index,grouped_by.values)
plt.show()
import matplotlib.pyplot as plt 
import pandas as pd 
# This is for if we create data 

# x = ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"]
# y = [100,90,190,200,300,700,800,]
# y1=[90,100,20,98,150,378,860]
# plt.plot(x,y,marker="o",ls="--",color = "red",label= "week1")
# plt.plot(x,y1,marker="*",ls="-",color = "green", label="Week2",alpha=0.5)
# plt.legend()
# plt.show()
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
# print(df)

grouped_data =df.groupby("Start Date")["Progress"].sum()
print(grouped_data)
plt.plot(grouped_data.index,grouped_data.values,marker= "o")
plt.show()
import pandas as pd 
# df = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
# print(df)
data_1 ={
    "Emp Id":["E01","E02","E03","E04","E05"],
    "Emp Names":["Rohan","Ali","Zain","Ahmed","Faisl"],
    "Age":[18,29,19,25,20],

}
data_2 ={
    "Emp Id":["E01","E07","E03","E08","E05"],
    "Salary":[20000,24000,50000,70000,80000]
}
df1= pd.DataFrame(data_1)
df2= pd.DataFrame(data_2)
print(df1)
print()
print(df2)
# print(pd.merge(df1,df2 ,on= "Emp Id"))#if we have no null values
print(pd.merge(left=df1,right= df2,on="Emp Id",how="left"))# This is called Left merge 
print(pd.merge(left=df1,right= df2,on="Emp Id",how="right"))# This is called Right merge 


# Hence we have to Concatenate  So we have to same data of both 

data_1 ={
    "Emp Id":["E01","E02","E03","E04","E05"],
    "Emp Names":["Rohan","Ali","Zain","Ahmed","Faisl"],
    "Age":[18,29,19,25,20],

}
data_2={
    "Emp Id":["E06","E07","E08","E09","E10"],
    "Emp Names":["chotu","Bunty","KAttur","JOhn","Jhatka"],
    "Age":[18,29,19,25,20],

}
df1=pd.DataFrame(data_1)
df2=pd.DataFrame(data_2)
print(pd.concat([df1,df2]))
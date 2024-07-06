import pandas as pd 
import numpy as np 
df = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
# print(df)
# Hence We can Add Transform a coloumn

df.loc[(df["Progress"] == 0 ),"Progress Staus"] = "No Progress"
df.loc[(df["Progress"] > 0 ),"Progress Staus"] = "Show Progress"
print(df)

# Hence we can Add more type of function 
df["Dep & Work "] = df ["Project Name"] +" & "+ df ["Task Name"]
print(df)

# ******************* Part 2 Of Coloumn Transformation *************


df = pd.read_excel("C:/Users/Sufi Computers/OneDrive/Desktop/New Microsoft Excel Worksheet.xlsx""")
# print(df)
df["Full Name "] = df["First Name "]+" "+df["Last Name "]
# print(df)
df["Bonous"]=(df["Salary "]/100*20)
print(df)


# We Create Data By our Self 
data = {
    "Months":["January","Febrary","March","April","May","June"]
}
a = pd.DataFrame(data)
def extract(value):
    return value[0:3]
a["Short Month"] = a ["Months"].map(extract)
print(a)
import pandas as pd 
df = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
print(df)
# We use groupby to access specific information easily 
gp = df.groupby(["Project Name","Days Required"]).agg({"Days Required":"count"})
print(gp)
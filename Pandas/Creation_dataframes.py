import pandas as pd 

# Creation of Data Frame Through Our Self 

data = {
    "Name":["Ali","Zain","Ahmed"],
    "Age":[18,20,23],
    "Salaries":[2000,4000,10000]
}
df = pd.DataFrame(data)
print(df)

# Extraction of data from any files  

data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx")
print(data)
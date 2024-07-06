import pandas as pd 
dict = {"Fruits":["Apple","Banana","Mangoes","Papaya"],
        "Price":[100,200,400,300],
        "Quantity":[12,10,20,40]
        }
df1 = pd.DataFrame(dict)
print(df1)
df2 = df1.copy()
df2.loc[0,"Price"]=150
df2.loc[1,"Price"]=170
df2.loc[2,"Price"]=190
df2.loc[3,"Price"]=160
df2.loc[0,"Quantity"]=15
df2.loc[1,"Quantity"]=10
df2.loc[2,"Quantity"]=20
df2.loc[3,"Quantity"]=90
print(df2)
print(df1.compare(df2,align_axis=0  ))
print(df1.compare(df2,keep_shape=True))
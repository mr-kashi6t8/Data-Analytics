import pandas as pd 
#   ****************** Pivoiting**************8
# dict = {
#     "Keys":["K1","K2","K1","K2"],
#     "Names":["Ali","Zain","Ahmed","Kashi"],
#     "Houses":["Red","Green","Blue","Orange"],
#     "Grades":["A","B","A","B"]
# }
# df1 = pd.DataFrame(dict)
# print(df1)
# # print(df1.pivot())
# print(df1.pivot_table(index="Keys",columns="Names",values=["Houses","Grades"]))
# *************** Melting***********************
dict = {
    
    "Names":["Ali","Zain","Ahmed","Kashi"],
    "Houses":["Red","Green","Blue","Orange"],
    "Grades":["A","B","A","B"]
}
df = pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Housese&Grades",value_name="Values"))
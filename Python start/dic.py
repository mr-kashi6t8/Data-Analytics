# ********************Dictionaries*********


# info ={
#     "key":"Value",
#     "Name":"Zain",
#     "Class":10,
#     "subject":{
#         "phy":13,
#         "chem":12
#     },
#     "age":18,
# }
# print(info["subject",])
# **************Iteration in dictionaries 

# Printing all the keys one by one 

# for i in info:
#     print(i)

# Printing all the values in dictionaries 

# for i in info:
#     print(info[i])

# using value function 

# for i in info.values():
#     print(i)

# For both values and key using item function 

# for i,x in info.items():
#     print(i,":",x)


# ****************Problem Solving In dictionaries **********
# WAP TO SORT THE VALUES OF DICTIONARIES 

# a = {
#     "a":10,
#     "b":8,
#     "c":1,
#     "d":3,
#     "e":98,
# }
# b = sorted(a.values())
# print(b)

# WAP TO STORE THE KEY AND THEIR SQAURE IN THE DICTIONARY  of 1 to 15 elements


# a ={}
# for i in range(1,16):
#     a[i]=i**2
# print(a)

# WAP TO MULTIPLY ALL THE ITEMS N THE DICTIONARY 

# a ={
#     "a":20,
#     "b":20,
#     "c":40,
#     "d":60,
# }
# product = 1
# for i in a:
#     product*=a[i]
# print(product)

# WAP TO SORT DICTIONARY BY KEY 

# a = {
#     12:"a",
#     1452:"b",
#     122:"c",
#     123:"d",
# }
# b = sorted(a.items())# its for items 
# c = sorted(a.keys())# its for key 
# print(c)

# WAP TO  CONVERT THE FOLLOWING DICTIONARY INTO JSONS FORMAT 


# student_data={"name":"Zain","age":14,"Class":12}
# import json
# data = json.dumps(student_data)
# print(data)
# print(type(data))

# WAP TO  ACCESS THE VALUE OF AGE FROM JSON DATA 


# import json
# student_data='{"name":"Zain","age":14,"Class":12}'#we makes it string 
# data = json.loads(student_data)
# print(data["age"])

# WAP TO PREETY PRINT OF JSON DATA 


# import json
# student_data={"name":"Zain","age":14,"Class":12}
# data = json.dumps(student_data,indent=4,separators=(",","="))
# print(data )

# sort the following json key and  write them into a file 


# import json
# student_data={"name":"Zain","age":14,"Class":12}
# f = open("demo.json","w")
# data = json.dumps(student_data,indent=4 ,sort_keys= True)
# f.write(data)
# print("The data Has been written into the file ")


# acces the nested key "marks from the given nested dictionaries "

# import json
# student_data="""{"students"":
#                     {"Grade":
#                         {"name":"David", "marks":87}
#                         }
#                         }"""
# data = json.dumps(student_data)
# print(data["students"]["grades"]["marks"])

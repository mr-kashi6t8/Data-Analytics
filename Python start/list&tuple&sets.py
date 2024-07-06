# ******************** LIST************************

# fruits = ["apple","Banana",12, "Watermellon"]
# # ******************List slicing**************
# a1 =fruits[1:3]
# a =fruits[:3]
# print(a1)
# print(fruits[::2])
# NegativeSlicing is same as strings in list 

#**************** List iteration ***************

# a = ["Zain","Ali","Ahmed ", "Nabil "]
# iteration using for looop

# for i in a:
#     print(i)

# iteration using for loop using range and length function
# for i in range(len(a)):
#     print (a[i])



# iteration using while loop 

# i = 0
# while i<len(a):
#     print(a[i])
#     i+=1


# iteration using short  for loop hand loop 

# [print(i) for i in a]

# ***************** List Functions*******************
# *****************List Comprehension*******************

# l1 =[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l1:
#     l2.append(i)
# print(l2)

# l1=[30,40,50,60]
# l3=[i for i in l1 if i >45]
# print(l3)
# *******************Problem Solving Realated to list***********
# A = ["rose","Indigo","Monica","Waterlily"]
# B = [13,7,12,10]
# WAP TO SWAP FIRST AND 4TH ELEMENT

# A[0],A[3]=A[3],A[0]
# print(A)

# WAP TO ADD A NEW VALUE AT POSITION 2ND

# A.insert(2,"watermellon")
# print(A)

# WAP TO DELETE A VALUE FROM 3RD POSITION

# A.pop(2)
# print(A)


# wAP TO MULTIPLY ALL NUMBER IN THE GIVEN LIST 

# mul = 1
# for i in B:
#     mul*=i
# print(mul)


# WAP TO CALCULATE THE LARGEST NUMBER

# largestnum=B[0]
# for i in B:
#     if i>largestnum:
#         largestnum=i
# print("The Largest Number  is ", largestnum)

# WAP TO CALCULATE THE SMALLEST NUMBER IN THE LIST

# smallest_num=B[0]
# for i in B:
#     if i<smallest_num:
#         smallest_num = i
# print("The smallest Num is ",smallest_num)

# ***********************TuPles *******************


# a =("apple","Banana","Mango",18,78,)
# We can itterate and use tuple same as list but tuples are unchangeable 
# Tuples can also be change into list so that we can add values in it 




# ************************** SETS ******************* 

# a = {"ALi","Zain ", "Ahmed ","Awais"}
# print(a)
# print(type(a))
# for x in a :
#     print(x)

# ***************Function of Sets ****************

# ******************PROBLEM SOLVING************

# WAP TO FIND MIN AND MAX IN THE SET 

# a ={12,13,3,7,9,10,15}
# largest = smallest = next(iter(a))
# for i in a :
#     if i>largest:
#         largest = i
#     if i<smallest:
#         smallest = i
# print("The largest numb in set is ",largest)
# print("The Smallest numb in set is ",smallest)

# WAP TO FIND COMMON ELEMENT IN THREE LIST 

# a=[4,5,6,7,8,9]
# b=[4,6,8,9]
# c=[4,6,7,8,10]

# a1=set(a)
# b1=set(b)
# c1=set(c)
# print(a1.intersection(b1 , c1))

# WAP TO  FIND DIFFERNCE BETWEEN 2 SETS
# a={4,5,6,7,8,9}
# b={4,6,8,9}
# print(a.difference(b))
# print(a.discard(9))

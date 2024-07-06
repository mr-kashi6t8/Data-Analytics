# ************************Introduction to loops *********************

# ********************FOR LOOPS *****************

# n = int(input("Enter a Number"))
# for i in range(1,11):
#     # print(f"The multiple of {n} by {i} is", n*i)
#     print(n,"x",i,"=",n*i)

# *************** While Loop************

# i = 1
# n = int(input("Enter a number "))
# while(i<=10):
#     print(n,"x",i,"=",n*i)
#     i+=1

#*************** While true loop*********

# while True:
#     num1 = int(input("Enter a number:")) 
#     num2 = int(input("Enter a number:"))
#     print("The sum of num 1 and num 2 is",num1 + num2) 
#     repeat = input("Do you want To stop the programm : ")
#     if repeat=="yes":
#         break

# **********************Nested Loop**********

# for i in range(1,4):
#     for j in range(1,11):
#         print(j, end="")
#     print()        

# for i in range(1,6):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# *********************For Loop with Conditional Statement***************

# for i in range (1,11):
#     if i == 3 :
#         print("Add this song to the fvrt")
#     else :
#         print(i)

# for i in range (1 , 101):
#     if i%8==0 and i%12==0 :
#         print(i)

# Hencewe use it with while loop 

n = 1
# while(n<=10):
#     if n==3:
#         print("Add this to fav")
#     else:
#         print(n)
#     n+=1

# n = 1
# while(n<=100):
#     if n%8==0 and n%12==0:
#         print(n)
#     n+=1

# ***************** Break And Continue statement 
# Continue 

# for i in range (1,10):
#     if i == 3:
#         continue
#     else:
#         print(i)


# Break

# for i in range(1,11):
#     if i == 4:
#         break
#     else:
#         print(i)


# Problem Solving By Loops

# WAP TO FIND THE SUM OF ALL THE EVEN NUMBER UPTO 50

# sum = 0
# for i in range(1,51):
#     if i%2==0:
#         sum+=i
# print("Sum of All the even numbers is ",sum)


# WAP TO WRITE FIRST 20 NUMBERS AND THEIR SQUARED NUMBER 

# for i in range(1,21):
#     print(i," ",i**2)

# WAP TO FIND FIRST 10 ODD NUMBERS USING WHILE LOOP


# n = 0
# sum = 0
# while(n<=20):
#     if n%2!=0:
#         sum+=n
#     n+=1
# print("The sum of first 10 0dd number is ",sum)


# WAP TO CHECK A NUMBER IS DIVISIBE BY BY 8 AND 12 UPTO 100

# for i in range(1,101):
#     if i%8==0 and i%12==0:
#         print(i)


# WAP TO CREATE A BILLING SYSTEM OF A SUPER MARKET

# while True:
#     name = input("Enter the customer name ")
#     total = 0
#     while True:
#         print("*** Enter Amount And Quantity***")
#         quantity= float(input("Enter Quantity of Item"))
#         amount= float(input("Enter amount of the Item"))
#         total+=amount*quantity
#         repeat=input("Do you wants to Add more items (Yes/No):")
#         if repeat=="no" or repeat=="No":
#             break
#     print("-"*40)        
#     print("Name:",name)
#     print("Amount to be Paid:",total,"$")
#     print("-"*40)
#     print("*********Happy Shopping ********")
#     repeat1= input("Do you wants to go to more Customer (Yes/No)")
#     if repeat=="No" or repeat =="no":
#         break
#
# **************** Slicing of String********************
# a = "harry potter and Globlet of Fire"
# print(a[0:5])
# print(a[6:12])
# print(a[:5])#if we dont wants to give start value
# n = "0123456"
# print(n[::2])
# print(n[:6:2])
# print(n[::-1])#if we wants to go back 
# *************Negative slicing*****
# print(a[-5:])

# ************Problem Solving*************
# WAP TO GET FIBONACCI SERIES UPTO 10 ELEMENT


# a = 0 
# b = 1
# n = int(input("Enter a Number Here "))
# if n==1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# WAP TO CHECK IF NUMBER IS  PRIME OR NOT


# num = int(input("Enter a Number : "))
# if num <= 1 :
#     print("Its not a prime number ")
# else:
#     for i in range (2,num):
#         if num%i==0:
#             print("Its Not a Prime Number")
#             break
#     else:
#         print("Its a Prime Number ")

# WAP TO CHECK IF ITS A PALINDROME OR NOT 

# num = int(input("Enter a Number "))
# temp = num
# reverse = 0
# while num>0:
#     dig = num%10
#     reverse=reverse*10+dig
#     num=num // 10


# if reverse == temp:
#     print("Its a Palindrome")
# else:
#     print("Its not a Palindrome ")

# WAP TO MAKE AREA CALCULATOR

# print("******Area Calulator**********")

# while True:
# 	print("""Press 1  to get the area of square 
# 	Press 2 to get the area of triangle
# 	Press 3 to get the area of Rectangele 
# 	Press 4 to get the Area of circle""")
# 	choice = int(input("Enter Your Choice"))
# 	if(choice==1):
# 		while True:
# 			side = float(input("Enter the length of side "))
# 			area = (side**2)
# 			print("The Area of square is ", area)
# 			repeat1 =input("Do You Wants to repeat The square?")
# 			if repeat1 == "no":
# 				break


# 	elif(choice==2):
# 		while True:
# 			base = float(input("Enter the base of triangle"))
# 			height = float(input("Enter the heighth of traingle "))
# 			area =1/2( base*height)
# 			print("The Area of triangle is ", area)
# 			repeat1 =input("Do You Wants to repeat The Triangle?")
# 			if repeat1 == "no":
# 				break		
# 	elif(choice==3):
# 		while True:
# 			length = float(input("Enter the length of Rectangele "))
# 			width = float(input("Enter the width of Rectangele "))
# 			area = (length*width)
# 			print("The Area of rectangle  is ", area)
# 			repeat1 =input("Do You Wants to repeat The Rectangle?")
# 			if repeat1 == "no":
# 				break
# 	elif(choice==4):
# 		while True:
# 			radius = float(input("Enter the radius of circle"))
# 			area = 3.14 *radius**2
# 			print('The area of cicle is ',area)
# 			repeat1 =input("Do You Wants to repeat The Square?")
# 			if repeat1 == "no":
# 				break
# 	repeat2=input("Do You wants to open menue again")
# 	if repeat2 == "no":
# 		break
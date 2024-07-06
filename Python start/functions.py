# ******************FUNCTIONS***************************

# def hello():
#     print("Hello World")
# hello()
# ********** Parameters and Aurguments********************

# def sum (a,b):
#     print(a+b)

# sum(45,14)

# *********arbitary aurguments*********

# def hello(*name):
#     print("My name is ",name[2])
# hello("zain","Ahmed","moon")


# ************** Return and Recursion Functions ************
# def hellow ():
#     return ("HelloWorld")

# print(hellow())

# ***************Recursion ****************

# def hello ():
#     print("hello")
#     return hello()

# print(hello())

# *******Factorial of number *********
# def fact(n):
#     if n==1 or n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# n = int(input("Enter a number"))
# print(f"The factorial of {n} is :" , fact(n))



# **************Lambda Function******************

# Annonymus function

# a = lambda b :b*5
# print(a(4))


# x = lambda a, b , c : a+b*c
# print(x(3,5,6))

# ************** Local and global Variables **************
# local variable 

# x = 12
# print("first variable is",x)
# def hello():
#     x = 24
#     return x

# print(hello())

# Global Variable 

# x = 12
# print("first variable is",x)
# def hello():
#     global x 
#     x = 24
#     return x

# print(hello())
# print(x)

# ****************Problem Solving*******************
# WAP TO find the maximum of 3 numbers in function 

# def max_numb(a,b,c):
#     max_value = a 
#     if b> max_value:
#         max_value = b
#     if c > max_value:
#         max_value = c
#         return max_value
    
# a , b, c = map(int,input("Enter 3 numbers ").split())#hence we can take 3 input continusoily 

# print("The largest number is ",max_numb(a, b ,c))

# WAP TO  PRINT AND CREATE CREATE A LIST  WHERE THE VALUES ARE SQUARE OF NUMBER BETWWEEN 1 AND 30 

# def create_list():
#     l=[]
#     for i in range (1,31):
#         l.append(i**2)
#     return l
# print(create_list())

# WAP TO CHECK NUMBER IS PRIME OR NOT

# def check_prime(n):
#     if n == 1 :
#         print("its not a prime number ")
#     if n == 2 :
#         print("its  a prime number ")
#     if n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 print("its not a prime number")
#                 break
#         else:
#             print("its a prime number ")

# n = int(input("Enter a number"))
# check_prime(n)



# WAP TO  FIND THE SUM OF ALL THE NUMBER IN THE LIST 

# def sum_list(n):
#     sum = 0 
#     for i in n :
#         sum+=i
#     return sum

# n =[12,13,14,15,16,17]
# print("the sum of given list is ",sum_list(n))


# WAP TO FIND THE FIBBONACCI SERIES USING RECURSION FUNCTION 
def fs(num):
    if num==1:
        return 0 
    elif num==2:
        return 1
    else:
        return (fs(num-1)+fs(num-2))
print(fs(8))

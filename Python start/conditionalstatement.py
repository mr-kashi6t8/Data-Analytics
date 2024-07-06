# CONDITIONAL STATEMENTS 

# marks = 10
# if(marks>90):
#     print("The Garde is A")
# elif(marks>50):
#     print("The Grade is B")
# else:
#     print("The Grade is F")

# Nested if statement 

# marks = 98
# if(marks>90):
#     print("The Garde is A")
#     if(marks>95):
#         print("You will get a phone ")
# elif(marks>50):
#     print("The Grade is B")
# else:
#     print("The Grade is F")


# Short Hand If statement   _____ One liner statement 

# marks = 99 
# if(marks>90): print("You will get a new phone ")

# Short Hand If else statement   _____ One liner statement 

# marks = 97
# print ("You will get a new phone ") if marks>=90 else print("No phone for a month")

# Problem solving 

# WAP to check if num is positive or negative 

# num = int(input("Enter a Number Here "))
# # print("The number is positive ")if(num>0) else print("Number is negative ")
# if num>0:
#     print("number is positive")
# elif num==0:
#     print("Number is zero neither positive nor negative ")
# else :
#     print("Number is negative ")

# WAP TO CHECK NUMBER IS ODD OR EVEN 

# num = int(input("ENter a number "))
# # print("Number is even ") if num%2==0 else print("Number is odd")
# if num%2==0:
#     print("Number is even  ")
# else :
#     print ("number is odd ")

# WAP TO CREATE AREA CALCULATOR 

# print("******Area Calulator**********")
# print("""Press 1  to get the area of square 
# Press 2 to get the area of triangle
# Press 3 to get the area of Rectangele 
# Press 4 to get the Area of circle""")
# choice = int(input("Enter Your Choice"))
# if(choice==1):
#     side = float(input("Enter the length of side "))
#     area = (side**2)
#     print("The Area of square is ", area)
# elif(choice==2):
#     base = float(input("Enter the base of triangle"))
#     heigth = float(input("Enter the heighth of traingle "))
#     area =1/2( base*height)
#     print("The Area of triangle is ", area)
# elif(choice==3):
#     length = float(input("Enter the length of Rectangele "))
#     width = float(input("Enter the width of Rectangele "))
#     area = (length*width)
#     print("The Area of rectangle  is ", area)
# elif(choice==4):
#     radius = float(input("Enter the radius of circle"))
#     area = 3.14 *radius**2
#     print('The area of cicle is ',area)


# WAP TO check a letter is vowel or not

# letter = input("Enter any letter")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("Its a vowel ")
# else:
#     print("Its not a vowel")

# WAP TO  CHECK NUMBER IS 1 DIGIT NUMBER IS 2 DITIGT OR SO ON 


# num = int(input("Enter a Number upto 5 digits "))
# if num>0 and num<9:
#     print("Its a single digit number")
# elif num>10 and num<99:
#     print("Its a double digit number")
# elif num>100 and num<999:
#     print("Its a triple digit number")
# elif num>1000 and num<9999:
#     print("Its a four digit number")
# else:
#     print("Its a five digit number")

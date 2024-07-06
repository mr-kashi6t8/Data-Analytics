import numpy as np 
# *******************Sorted function ***********
# arr = np.array([[12,17,20,2,8,9],[23,19,13,47,87,50]])
# print(np.sort(arr))

# Search function in array 

# arr = np.array([7,4,5,8,9])
# arr1=np.sort(arr)
# ss=np.searchsorted(arr1,7)
# # s=np.where(arr%7==0)
# # s = np.where(arr%2==0)
# # print(s)
# print(ss)

# Filter Function in array 
arr = np.array([20,30,40,50])
# This is one way 

# fa = [True,False,True,False]
# new =arr[fa]
# print(new)
# fa = arr>35
fa = arr%2==0
new = arr[fa]
print(new)
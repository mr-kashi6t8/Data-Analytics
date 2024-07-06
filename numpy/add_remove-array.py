import numpy as np 
# add or remove elements in an array

# # arr1 =np.array([12,40,60,80])
# arr1 =np.array([[12,40],[60,80]])
# # print(np.append(arr1,19)) 
# print(np.append(arr1,[19,100])) 

# Insert value 

# arr1 =np.array([12,40,60,80])
arr1 =np.array([[12,40],[60,80]])

# print(np.insert(arr1,[1,2],[50,100],axis=0))
# Delete Value by this methods 
print(np.delete(arr1,[1],axis=1))


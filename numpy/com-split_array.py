import numpy as np 
#****************** Concatenate*********


# arr1 = np.array([[2,4],[6,8]])
# arr2= np.array([[3,9],[12,15]])
# # print(np.concatenate([arr1,arr2]))
# print(np.concatenate([arr1,arr2],axis=0)) # Through axis 
# print(np.hstack([arr1,arr2]))# Horizontal conactenation
# print(np.vstack([arr1,arr2]))# Vertical conactenation


# ********************Split Array ***********
arr1 = np.array([[2,4],[6,8]])
# arr2 = np.array([[10,9],[4,12]])
# arr1=np.array([20,25,30,40,50])
print(np.array_split(arr1,3))
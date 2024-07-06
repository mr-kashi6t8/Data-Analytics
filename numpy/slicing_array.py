import numpy as np

# # ****************************** Normal Slicing in array ***************
# arr = np.array([12,13,14])
# # we already see thse type of silicing in list etc 
# print(arr[0:1])

# ***************Slicing Of 2 D arrays in numpy *******************

# arr =np.array([[12,13,14,15],[17,18,19,20],[90,70,80,40]])
# print(arr[0:2,0:2])
# print(arr[1,:3])#hence 1 st we have to add the index numb of array then we have to add index of numbers 
# print(arr[2,0:2])# hence same in that case 

# ******************Artribute of array $ Inspection of an array **********************

arr =np.array([[12,13,14,15],[17,18,19,20],[90,70,80,40]])

# print(np.shape(arr))
# print(np.size(arr))
# print(np.ndim(arr))
# print(arr.dtype)
# print(len(arr))
print(arr.astype(float))# hence we convert it into any data type  


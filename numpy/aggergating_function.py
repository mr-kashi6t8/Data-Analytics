import numpy as np 

# arr = np.array([12,13,14,15,16])
# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.size(arr))
# print(np.mean(arr))
# print(np.cumsum(arr))
# print(np.cumprod(arr))

# For  Double Values 
a = [12,13,14,15]
b = [2,3,4,18]
price = np.array(a)
quantity = np.array(b)
print(price,"\n",quantity)
print()
c = np.cumprod([price,quantity],axis = 0)
print(c)
print(c[1].sum())
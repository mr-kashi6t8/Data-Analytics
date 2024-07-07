import matplotlib.pyplot as plt 
x = [23,46,34,23,24,78]
y = [22,46,7,23,90,78]
y1 = [14,4,34,3,2,78]
plt.figure(figsize=[5,3])
plt.plot(x,y,label="male")
plt.plot(x,y1,label="female")
plt.legend()
plt.show()
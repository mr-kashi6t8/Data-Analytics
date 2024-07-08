import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [47,25,24,32,45]
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Age")
# plt.show()

x = [6,7,8,9,10]
y = [75,50,24,20,40]
plt.subplot(2,2,2)
plt.plot(x,y)
plt.title("Weight")

# plt.show()

x = [6,7,8,9,10]
y = [75,50,24,20,40]
plt.subplot(2,2,3)# rows ,Coloumn ,Chart No 
plt.plot(x,y)
plt.title("Money")
# plt.show()

x = [6,7,8,9,10]
y = [75,50,24,20,40]
plt.subplot(2,2,4)
plt.plot(x,y)
plt.show()
plt.title("Wealth")
plt.suptitle("Employee Data ")
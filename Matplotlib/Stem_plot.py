import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

# x = [12,34,76,89,98,76,35,46,76]
# plt.stem(x,linefmt="--",markerfmt="D",orientation="horizontal")
# plt.show()
# If we plot it on Data Set
data = pd.read_excel("C:/Users/Sufi Computers/Downloads/Project-Management-Sample-Data.xlsx""")
df = pd.DataFrame(data)
print(df)
plt.stem(df["Days Required"],linefmt="--")
plt.title("Variation Of Days Requirements",fontsize=20)
plt.plot(df["Days Required"])
plt.show()
import pandas as pd
from matplotlib import pyplot as plt

x=[1,2,3,4,5]
y=[4,3,2,5,6]
z=[10,5,7,8,9]
plt.title("Test Plot")
plt.plot(x,y, marker='o', linestyle='--',color='r')
plt.plot(y,z)
plt.xlabel("X")
plt.ylabel("Y and Z")
plt.legend(["y","z"],loc="lower right")
plt.show()

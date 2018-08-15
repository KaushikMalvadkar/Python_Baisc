import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(1,50)
y=np.random.randn(1,50)
plt.scatter(x,y,s=30)
plt.legend(loc="lower right")
plt.show()

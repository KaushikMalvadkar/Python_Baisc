import numpy as np
import matplotlib.pyplot as plt

data=np.random.normal(2.0,2.5,1000)

plt.hist(data)
plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

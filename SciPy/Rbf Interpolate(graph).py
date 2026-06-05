import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import Rbf

x = np.arange(10)
y = 2 ** x + np.sin(x) + 1
f = Rbf(x, y)
x_new = np.arange(2.1, 3, 0.1)
y_new = f(x_new)

plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_new, '-', label='RBF Interpolation')
plt.legend()
plt.show()
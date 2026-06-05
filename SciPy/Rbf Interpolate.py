from scipy.interpolate import Rbf
import numpy as np

x = np.arange(10)
y = 2 ** x + np.sin(x) + 1
f = Rbf(x, y)
a = f(np.arange(2.1, 3, 0.1))
print(a)
from scipy.interpolate import Rbf
import numpy as np
x = np.arange(10)
y = x**2 + np.sin(x)
rbf = Rbf(x, y)
print(rbf(2.5))
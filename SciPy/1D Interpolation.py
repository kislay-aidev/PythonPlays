from scipy.interpolate import interp1d
import numpy as np
x = np.arange(10)
y = 2 * x + 1

f = interp1d(x, y)
a = f (np.arange(2.1, 3, 0.1))
print(a)
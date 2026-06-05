from scipy.interpolate import UnivariateSpline
import numpy as np

x = np.arange(10)
y = x**2 + np.sin(x)
spline = UnivariateSpline(x, y)
print(spline(2.5))
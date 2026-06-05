#printing constant value of PI
from scipy.optimize import minimize as mini
def eqn (x):
    return x**2 + x + 2
mymin = mini(eqn, 0, method = 'BFGS')
print(mymin)
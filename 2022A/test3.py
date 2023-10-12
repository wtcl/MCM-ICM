from sympy import *
import sympy
from scipy.optimize import fmin,fminbound,minimize,minimize_scalar
import numpy as np
from sympy.solvers.solveset import invert_complex, invert_real

x=symbols("x", real=True,positive=True)
# print(x.is_integer)
# y=symbols('y')
# f=Function("f")
# y=Function("y")
# n=Symbol('n', integer=True)
# f=y(n)-2*y(n-1)-5*y(n-2)
# pprint(rsolve(f,y(n),[1,4]))
# sv=solve(x**4+2*x-6)
# pprint(sv)
def f(x):
    return 2*x**4+x**3+x**2+x+1000-1005.1051+10000
res=solve(2*x**4+x**3+x**2+x+1000-1005.1051+10000)
print(res)
newres=[]
for i in res:
    if isinstance(i,sympy.core.numbers.Float) or isinstance(i,sympy.core.numbers.Integer):
        newres.append(i)
print(newres)
if newres.__len__()==0:
    res = minimize_scalar(f,  bounds=(0,10000000000000),method='bounded')
    print(res)
import random
import time
# from itertools import permutations,combinations,product
from sympy import *
import sympy
from scipy.optimize import fmin,fminbound,minimize,minimize_scalar
import numpy as np

stime=time.time()
# a=[5,10,15]
# def up_down(t):
#     return random.randint(0,5),random.randint(10,40)
#
# tv={}
# for j in range(100):
#     t = 0
#     tt, ll = up_down(j)
#     t += tt
#     if ll+j<100:
#         t+=(100-ll)/10
#         print(j,t)
        # tv[str(j)]=t
# print(list(tv.values()).index(max(list(tv.values()))))

x=Symbol("x", real=True,positive=True)
y=Symbol("y", real=True,positive=True)
def f(z):
    return z**2+z+1000-1005.1051+10000
res=solve(x**2+x+1000-1005.1051+10000+3*y**2, real=True,positive=True)
print(res)
newres=[]
for i in res:
    if isinstance(i,sympy.core.numbers.Float) or isinstance(i,sympy.core.numbers.Integer):
        newres.append(i)
print(newres)
if newres.__len__()==0:
    res = minimize_scalar(f,  bounds=(0,100000),method='bounded')
    print(res.x)

etime=time.time()
print(etime-stime)
import pandas as pd
from sympy import *

t=0

cd = 0.27
m = 75
g = 9.8
rou = 1.2
A = 0.5
miu = 0.03
dx=10
t1=1620.94259507461
t2=485.466261664237+t1

def fun(t):
    return 0.00001 * t ** 2 - 0.0827 * t + 492.31

V=[0]
X=[0]
T=[0]
P=[0]

while X[-1]<43300:
    if T[-1] < t1:
        P.append(fun(T[-1]))
    elif T[-1] < t2:
        P.append(fun(T[-1] - t1))
    else:
        P.append(fun(T[-1] - t2))
    cp = P[-1]
    v0 = Symbol("v0", positive=True, real=True)
    res = solve((cp - (m * g * sin(0) + miu * m * g * cos(0) + cd * rou * A * v0 ** 2) * v0))
    v0 = res[0]
    V.append(v0)
    X.append(dx+X[-1])
    dt=dx/v0
    t=t+dt
    T.append(t)
newdata=pd.DataFrame({"t":T,"V":V,"X":X,"P":P})
newdata.to_csv("8.2.csv",index=False)

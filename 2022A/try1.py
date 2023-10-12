import pandas as pd
from sympy import *


def get_angle_tokyo_men(ss):
    if ss<3000:
        return asin(-150/3000)
    elif ss<5000:
        return 0
    elif ss<10300:
        return asin(221/5300)
    elif ss<15000:
        return asin(-176/4700)
    elif ss<15500:
        return 0
    elif ss<17500:
        return asin(90/2000)
    elif ss<22000:
        return 0
    elif ss<25500:
        return asin(-141/3500)
    elif ss<27000:
        return 0
    elif ss<32400:
        return asin(221/5400)
    elif ss<36400:
        return asin(-176/4000)
    elif ss<37600:
        return 0
    elif ss<39600:
        return asin(90/2000)
    else:
        return 0

def get_angle_tokyo_women(ss):
    if ss<3500:
        return asin(-150/3500)
    elif ss<5000:
        return 0
    elif ss<10300:
        return asin(221/5300)
    elif ss<15000:
        return asin(-176/4700)
    elif ss<15500:
        return 0
    elif ss<17500:
        return asin(90/2000)
    else:
        return 0


dx = 10
sit = 0
cd = 0.27
m = 75
g = 9.8
rou = 1.2
A = 0.5
miu = 0.03
a1 = 7 * exp(-6)
a2 = 0.0023

X=[]
V=[]
T=[]
WW=[]


def test(w0,t,v0,tP):
    cp = 0.00001*t**2-0.0827*t+492.31
    # print("cp: ",cp)

    # v0 = Symbol("v0", positive=True, real=True)
    # res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
    # v0 = res[0]

    # print('v0: ', v0)
    # print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
    sit = get_angle_tokyo_men(X[-1])
    B0 = -m * v0 ** 2 / (2 * dx) + m * g * sin(sit) + miu * m * g * cos(sit) + 0.25 * cd * rou * A * v0 ** 2
    B1 = 0.5 * cd * rou * A * v0
    B2 = m / (2 * dx) + 0.25 * cd * rou * A
    C0 = 0.5 * B0 * v0
    C1 = 0.5 * B0 + 0.5 * B1 * v0
    C2 = 0.5 * B2 * v0 + 0.5 * B1
    C3 = 0.5 * B2

    Pmax = -212.9*ln(t-tP+1)+1665.3
    # print("Pmax: ", int(Pmax))

    v1 = symbols("v1", positive=True, real=True)
    C0, C1 = float(C0), float(C1)
    # print("C0 C1 C2 C3 Pmax\n", float(B0), C0, C1, C2, C3,Pmax)
    res = solve((C0 + C1 * v1 + C2 * v1 ** 2 + C3 * v1 ** 3 - Pmax))
    v1 = res[0]
    print("v1: ", v1)
    # print(C0+C1*v1+C2*v1**2+C3*v1**3)

    dt = 2 * dx / (v0 + v1)
    # print("dt: ", dt)

    w1 = w0 - (Pmax - cp) * dt
    print('w1: ', float(w1))

    P = (w0 - w1) * (v0 + v1) / (2 * dx)
    # print('P: ', float(P))

    return w1,t+dt,v1,dx

def test1(w0,t,v0):
    cp = 0.00001*t**2-0.0827*t+492.31
    # print("cp: ",cp)

    # v0 = Symbol("v0", positive=True, real=True)
    # res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
    # v0 = res[0]

    # print('v0: ', v0)
    # print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
    sit = get_angle_tokyo_men(X[-1])
    B0 = -m * v0 ** 2 / (2 * dx) + m * g * sin(sit) + miu * m * g * cos(sit) + 0.25 * cd * rou * A * v0 ** 2
    B1 = 0.5 * cd * rou * A * v0
    B2 = m / (2 * dx) + 0.25 * cd * rou * A
    C0 = 0.5 * B0 * v0
    C1 = 0.5 * B0 + 0.5 * B1 * v0
    C2 = 0.5 * B2 * v0 + 0.5 * B1
    C3 = 0.5 * B2

    Pmax = cp
    # print("Pmax: ", int(Pmax))

    v1 = symbols("v1", positive=True, real=True)
    C0, C1 = float(C0), float(C1)
    # print("B0 B1 B2 C0 C1 C2 C3\n", float(B0), B1, B2, C0, C1, C2, C3)
    res = solve((C0 + C1 * v1 + C2 * v1 ** 2 + C3 * v1 ** 3 - Pmax))
    v1 = res[0]
    print("v1: ", v1)
    # print(C0+C1*v1+C2*v1**2+C3*v1**3)

    dt = 2 * dx / (v0 + v1)
    # print("dt: ", dt)

    w1 = w0 - (Pmax - cp) * dt
    print('w1: ', float(w1))

    P = (w0 - w1) * (v0 + v1) / (2 * dx)
    # print('P: ', float(P))

    return w1,t+dt,v1,dx


t = 1
w0 = 24000
v0=10
V.append(v0)
WW.append(w0)
T.append(1)
X.append(0)
bjt=-1
while X[-1]<44200:
    vvv=V[-1]
    while WW[-1]>=0 and X[-1]<44200:
        w0, t, v0, xx = test(WW[-1], T[-1], V[-1],bjt)
        V.append(v0)
        WW.append(float(w0))
        X.append(xx + X[-1])
        T.append(t)

    WW[-1]=0

    while V[-1] >= ((max(V) - vvv) / 2.73 + vvv) and X[-1]<44200:
        w0, t, v0, xx = test1(WW[-1], T[-1], V[-1])
        V.append(v0)
        WW.append(float(w0))
        X.append(xx + X[-1])
        T.append(t)
        # print("v: ",V[-1])

    cp = 0.00001 * T[-1] ** 2 - 0.0827 * T[-1] + 492.31

    while WW[-1] < 24000 and X[-1]<44200:
        sit = get_angle_tokyo_men(X[-1])
        v0 = Symbol("v0", positive=True, real=True)
        res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
        v0 = res[0]
        V.append(v0)
        dt = 2 * dx / (V[-1] + v0)
        T.append(T[-1] + dt)
        cp = 0.00001 * T[-1] ** 2 - 0.0827 * T[-1] + 492.31
        X.append(X[-1] + dx)
        WW.append(float(WW[-1] + (cp*0.2) * dt))
        print("W:",WW[-1])
    bjt=T[-1]

print(X)
print(V)
print(WW)
print(T)

data=pd.DataFrame({"T":T,"X":X,"V":V,"WW":WW})
data.to_csv("data_change.csv",index=False)
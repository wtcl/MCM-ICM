import pandas as pd
from sympy import *
import time

times=time.time()
dx = 10
sit = 0.0001
cd = 0.27
m = 75
g = 9.8
rou = 1.2
A = 0.5
miu = 0.03
a1 = 7 * exp(-6)
a2 = 0.0023



def our_road(ss):
    if ss<5000:
        return 0.02
    elif ss<10200:
        return 0
    elif ss<12700:
        return -0.04
    elif ss<15510:
        return 0
    elif ss<15510+5000:
        return 0.02
    elif ss<15510+10200:
        return 0
    elif ss<15510+12700:
        return -0.04
    elif ss<15510+15510:
        return 0
    elif ss<15510+15510+5000:
        return 0.02
    elif ss<15510+15510+10200:
        return 0
    elif ss<15510+15510+12700:
        return -0.04
    else:
        return 0

def corner(ss):
    if 5000<=ss<5040:
        X.append(X[-1]+10)
        V.append(sqrt(9.8*120*tan(28/180)/3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu*m*g*V[-1]+0.5*cd*rou*A*V[-1]**3))
        return 1
    elif 7540<=ss<7620:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 120 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 10120<=ss<10200:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 160 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 12700<=ss<12800:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 200 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15300<=ss<15500:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 300 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+5000<=ss<15510+5040:
        X.append(X[-1]+10)
        V.append(sqrt(9.8*120*tan(28/180)/3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+7540<=ss<15510+7620:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 120 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+10120<=ss<15510+10200:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 160 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+12700<=ss<15510+12800:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 200 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15300<=ss<15510+15500:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 300 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15510+5000<=ss<15510+15510+5040:
        X.append(X[-1]+10)
        V.append(sqrt(9.8*120*tan(28/180)/3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15510+7540<=ss<15510+15510+7620:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 120 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15510+10120<=ss<15510+15510+10200:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 160 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15510+12700<=ss<15510+15510+12800:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 200 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    elif 15510+15510+15300<=ss<15510+15510+15500:
        X.append(X[-1] + 10)
        V.append(sqrt(9.8 * 300 * tan(28 / 180) / 3.141592653589793))
        WW.append(WW[-1])
        T.append(T[-1]+(10 / V[-1]))
        PP.append((miu * m * g * V[-1] + 0.5 * cd * rou * A * V[-1] ** 3))
        return 1
    else:
        return 0





X=[]
V=[]
T=[]
WW=[]
PP=[]


def test(w0,t,v0,tP):
    cp = (0.00001*t**2-0.0827*t+492.31)
    # print("cp: ",cp)

    # v0 = Symbol("v0", positive=True, real=True)
    # res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
    # v0 = res[0]

    # print('v0: ', v0)
    # print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
    sit = our_road(X[-1])
    # sit=0.04
    B0 = -m * v0 ** 2 / (2 * dx) + m * g * sin(sit) + miu * m * g * cos(sit) + 0.25 * cd * rou * A * v0 ** 2
    B1 = 0.5 * cd * rou * A * v0
    B2 = m / (2 * dx) + 0.25 * cd * rou * A
    C0 = 0.5 * B0 * v0
    C1 = 0.5 * B0 + 0.5 * B1 * v0
    C2 = 0.5 * B2 * v0 + 0.5 * B1
    C3 = 0.5 * B2

    Pmax = (-212.9*ln(t-tP+1)+1665.3)
    # print("Pmax: ", int(Pmax))
    if sit<-0.03:
        Pmax=0.9*Pmax
    elif sit<0.03:
        Pmax=0.8*Pmax
    else:
        Pmax=0.7*Pmax

    v1 = symbols("v1", positive=True, real=True)
    C0, C1 = float(C0), float(C1)
    # print("B0 B1 B2 C0 C1 C2 C3 Pmax\n", float(B0), float(B1),float(B2),C0, C1, C2, C3,Pmax)
    res = solve((C0 + C1 * v1 + C2 * v1 ** 2 + C3 * v1 ** 3 - Pmax))
    v1 = res[0]
    #print("v1: ", v1)
    # print(C0+C1*v1+C2*v1**2+C3*v1**3)

    dt = 2 * dx / (v0 + v1)
    P = Pmax

    if Pmax>=cp:
        w1 = w0 - (Pmax - cp) * dt
    else:
        return w0,t+dt,v1,dx,0,P

    return w1,t+dt,v1,dx,1,P

def test1(w0,t,v0):
    cp = (0.00001*t**2-0.0827*t+492.31)
    # print("cp: ",cp)

    # v0 = Symbol("v0", positive=True, real=True)
    # res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
    # v0 = res[0]

    # print('v0: ', v0)
    # print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
    sit = our_road(X[-1])
    # sit=0.04
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
    # print("v1: ", v1)
    # print(C0+C1*v1+C2
    # *v1**2+C3*v1**3)

    dt = 2 * dx / (v0 + v1)
    # print("dt: ", dt)

    w1 = w0 - (Pmax - cp) * dt
    # print('w1: ', float(w1))

    P =cp
    # print('P: ', float(P))

    return w1,t+dt,v1,dx,P

def test2(w0,t,v0):
    cp = (0.00001*t**2-0.0827*t+492.31)
    # print("cp: ",cp)

    # v0 = Symbol("v0", positive=True, real=True)
    # res = solve((cp - (m * g * sin(sit) + miu * m * g * cos(sit) + cd * rou * A * v0 ** 2) * v0))
    # v0 = res[0]

    # print('v0: ', v0)
    # print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
    sit = our_road(X[-1])
    # sit=0.04
    B0 = -m * v0 ** 2 / (2 * dx) + m * g * sin(sit) + miu * m * g * cos(sit) + 0.25 * cd * rou * A * v0 ** 2
    B1 = 0.5 * cd * rou * A * v0
    B2 = m / (2 * dx) + 0.25 * cd * rou * A
    C0 = 0.5 * B0 * v0
    C1 = 0.5 * B0 + 0.5 * B1 * v0
    C2 = 0.5 * B2 * v0 + 0.5 * B1
    C3 = 0.5 * B2

    Pmax = cp*0.8
    # print("Pmax: ", int(Pmax))

    v1 = symbols("v1", positive=True, real=True)
    C0, C1 = float(C0), float(C1)
    # print("B0 B1 B2 C0 C1 C2 C3\n", float(B0), B1, B2, C0, C1, C2, C3)
    res=[]
    # with eventlet.Timeout(2, False):
    res = solve((C0 + C1 * v1 + C2 * v1 ** 2 + C3 * v1 ** 3 - Pmax))
    # if len(res)==0:
    #     res=[V[-1]]
    v1 = res[0]
    # print("v1: ", v1)
    # print(C0+C1*v1+C2*v1**2+C3*v1**3)

    dt = 2 * dx / (v0 + v1)
    # print("dt: ", dt)

    w1 = w0 - (Pmax - cp) * dt

    P = 0.8*cp

    return w1,t+dt,v1,dx,P

t = 1
w0 = 24000
v0=10
V.append(v0)
WW.append(w0)
T.append(1)
X.append(0)
PP.append(0)
bjt=-1
num=0
while X[-1]<46530:
    Pmax_cp=1
    num+=1
    vvv=V[-1]
    while WW[-1]>=0 and X[-1]<46530 and Pmax_cp==1:
        w0, t, v0, xx ,Pmax_cp,p= test(WW[-1], T[-1], V[-1],bjt)
        V.append(v0)
        WW.append(float(w0))
        X.append(xx + X[-1])
        T.append(t)
        PP.append(p)
        print("v加：",V[-1])
        while corner(X[-1]):
            print("转弯：",X[-1])
    if WW[-1]<0:
        WW[-1]=0

    while V[-1] >= ((max(V) - vvv) / 2.73 + vvv) and X[-1]<46530:
        w0, t, v0, xx ,p= test1(WW[-1], T[-1], V[-1])
        V.append(v0)
        WW.append(float(w0))
        X.append(xx + X[-1])
        T.append(t)
        print("v减:",V[-1])
        PP.append(p)
        while corner(X[-1]):
            print("转弯：",X[-1])

    while WW[-1] < 24000*(0.95)**(num) and X[-1]<46530:
        w0, t, v0, xx ,p= test2(WW[-1], T[-1], V[-1])
        V.append(v0)
        WW.append(float(w0))
        X.append(xx + X[-1])
        T.append(t)
        PP.append(p)
        print(WW[-1])
        while corner(X[-1]):
            print("转弯：",X[-1])
    bjt=T[-1]
    print("X:",X[-1])

print("over")
print("t:",T[-1])

data=pd.DataFrame({"T":T,"X":X,"V":V,"WW":WW,"P":PP})
data.to_csv("./our_road_optimize.csv",index=False)
timee=time.time()
print(timee-times)

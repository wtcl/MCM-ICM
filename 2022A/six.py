import pandas as pd
from sympy import *
data=pd.read_csv("./solo_cp.csv")

print(data)
dx = 10
sit = 0.0001
cd = 0.1
m = 75
g = 9.8
rou = 1.2
A = 0.5
miu = 0.03
a1 = 7 * exp(-6)
a2 = 0.0023
sum=0
P=[0]
Wo=[2644700]
for i in range(1,data.shape[0]):
    v0=data.iat[i,1]
    t=data.iat[i,0]
    B0 = -m * v0 ** 2 / (2 * dx) + m * g * sin(sit) + miu * m * g * cos(sit) + 0.25 * cd * rou * A * v0 ** 2
    B1 = 0.5 * cd * rou * A * v0
    B2 = m / (2 * dx) + 0.25 * cd * rou * A
    C0 = 0.5 * B0 * v0
    C1 = 0.5 * B0 + 0.5 * B1 * v0
    C2 = 0.5 * B2 * v0 + 0.5 * B1
    C3 = 0.5 * B2
    cP=C0 + C1 * v0 + C2 * v0 ** 2 + C3 * v0 ** 3
    P.append(cP)
    sum+=(t-data.iat[i-1,0])*cP
    Wo.append(2644700-sum)

# wo2=994222.153096558
# cp=-14.45*ln(t)+512.3
data["P"]=P
data["wo2"]=Wo
data.to_csv("./solo_cp_six.csv")


from sympy import *

t=0
w0=9758
cp=234
dx=10
sit=0
cd=0.27
m=75
g=9.8
rou=1.2
A=0.5
miu=0.25
a1=7*exp(-6)
a2=0.0023

v0=Symbol("v0",positive=True,real=True)
res=solve((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))
v0=res[0]
print('v0: ',v0)
# print((cp*exp(-t/100)-(m*g*sin(sit)+miu*m*g*cos(sit)+cd*rou*A*v0**2)*v0))

A0=2*w0+cp*exp(-t/100)-v0/(2*dx*a1)+a2/a1
A1=-1/(2*dx*a1)
B0=-m*v0**2/(2*dx)+m*g*sin(sit)+miu*m*g*cos(sit)+0.25*cd*rou*A*v0**2
B1=0.5*cd*rou*A*v0
B2=m/(2*dx)+0.25*cd*rou*A
C0=-A0+0.5*B0*v0
C1=-A1+0.5*B0+0.5*B1*v0
C2=0.5*B2*v0+0.5*B1
C3=0.5*B2


v1=symbols("v1",positive=True,real=True)
C0,C1=float(C0),float(C1)
print("A0 A1 B0 B1 B2 C0 C1 C2 C3\n",float(A0),float(A1),float(B0),B1,B2,C0,C1,C2,C3)
res=solve((C0+C1*v1+C2*v1**2+C3*v1**3))
v1=res[0]
print("v1: ",v1)
# print(C0+C1*v1+C2*v1**2+C3*v1**3)

w1=(v0+v1)/(2*dx*a1)-a2/a1-w0
print('w1: ',float(w1))

P=(w0-w1)*(v0+v1)/(2*dx)
print('P: ',float(P))


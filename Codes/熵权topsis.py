import math
import pandas as pd
import os

file_path = os.path.join("1.csv")
list=['A','B','C','D','E','F']
data = pd.read_csv(open(file_path,'r',encoding='utf-8'),sep=',',usecols=list)
print(data)

def gui01z(A,list):    # 正向标准化
    list = list
    h=A.shape[0]
    l=A.shape[1]
    B=A.loc[:,:]
    for j in range(l):
        maxx=max(A[list[j]])
        minn=min(A[list[j]])
        for i in range(h):
            B.iat[i,j]=(float(A.iat[i,j])-minn)/(maxx-minn)
    print('B:\n',B)
    return B


Bdata=gui01z(data,list)
Y=data
h=data.shape[0]
l=data.shape[1]
for j in range(l):
    s=sum(Bdata[list[j]])
    for i in range(h):
        Y.iat[i,j]=Bdata.iat[i,j]/s
print('Y:\n',Y)

E=[]
for j in range(l):
    s=0
    for i in range(h):
        if Bdata.iat[i,j]==0.00:
            s=s+0
        else:
            s=s+Bdata.iat[i,j]*math.log10(Bdata.iat[i,j])
    E.append(s*(-1/math.log(h)))
print('E:\n',E)

W=[]
for i in range(len(E)):
    W.append((1-E[i])/(len(E)-sum(E)))
print('W:\n',W)

score=[]
for i in range(h):
    s=0
    for j in range(l):
        s=s+Y.iat[i,j]*W[j]
    score.append(s*100)
print('score:\n',score)

Bdata=gui01z(data)
h=Bdata.shape[0]
l=Bdata.shape[1]
Dz=[]
Df=[]
for i in range(h):
    d0=0
    d1=0
    for j in range(l):
        d0=d0+W[j]*(Bdata.iat[i,j]-max(Bdata[list[j]]))**2
        d1=d1+W[j]*(Bdata.iat[i, j] - min(Bdata[list[j]])) ** 2
    Dz.append(d0)
    Df.append(d1)
print('Dz:\n',Dz)
print('Df:\n',Df)

sc=[]
for i in range(h):
    sc.append(Df[i]/(Df[i]+Dz[i]))
print('sc:\n',sc)


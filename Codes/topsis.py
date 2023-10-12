import math
import pandas as pd
import os

file_path = os.path.join("1.csv")
list=['A','B','C','D','E','F']
data = pd.read_csv(open(file_path,'r',encoding='utf-8'),sep=',',usecols=list)
print(data)

def gui01z(A):    # 正向标准化
    list = ['A', 'B', 'C', 'D', 'E', 'F']
    h=A.shape[0]
    l=A.shape[1]
    B=A.loc[:,:]
    for j in range(l):
        maxx=max(A[list[j]])
        minn=min(A[list[j]])
        for i in range(h):
            B.iat[i,j]=(float(A.iat[i,j])-minn)/(maxx-minn)
    print(B)
    return B

Bdata=gui01z(data)
h=Bdata.shape[0]
l=Bdata.shape[1]
Dz=[]
Df=[]
for i in range(h):
    d0=0
    d1=0
    for j in range(l):
        d0=d0+(Bdata.iat[i,j]-max(Bdata[list[j]]))**2
        d1=d1+(Bdata.iat[i, j] - min(Bdata[list[j]])) ** 2
    Dz.append(d0)
    Df.append(d1)
print(Dz)
print(Df)

sc=[]
for i in range(h):
    sc.append(Df[i]/(Df[i]+Dz[i]))
print(sc)
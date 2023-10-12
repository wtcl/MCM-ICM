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


def gui01f(A):    # 负向标准化
    list = ['A', 'B', 'C', 'D', 'E', 'F']
    h=A.shape[0]
    l=A.shape[1]
    B=A.loc[:,:]
    for j in range(l):
        maxx=max(A[list[j]])
        minn=min(A[list[j]])
        for i in range(h):
            B.iat[i,j]=(maxx-float(A.iat[i,j]))/(maxx-minn)
    print(B)
    return B

def zscore(A):    # z-score标准化
    list = ['A', 'B', 'C', 'D', 'E', 'F']
    h=A.shape[0]
    l=A.shape[1]
    B=A.loc[:,:]
    for j in range(l):
        avr=sum(A[list[j]])/h
        S=A[list[j]].std()
        for i in range(h):
            B.iat[i,j]=(float(A.iat[i,j])-avr)/S
    print(B)
    return B

zscore(data)

# https://blog.csdn.net/qq_42374697/article/details/106742248

import pandas as pd
import os
import numpy as np

file_path = os.path.join("1.csv")
list=['A','B','C','D','E','F']
data = pd.read_csv(open(file_path,'r',encoding='utf-8'),sep=',',usecols=list)
print(data)

# 整秩法，考虑因每列数据重复导致的冲突,并且将其折中化
def zzf(data,list):
    h = data.shape[0]
    l = data.shape[1]
    R = pd.DataFrame(np.zeros((h, l)), columns=list)
    for j in range(l):
        slist0 = sorted(data[list[j]])
        slist1 = sorted(data[list[j]], reverse=True)
        print(slist0)
        print(slist1)
        c = len(slist0)
        for i in range(h):
            R.iat[i, j] = (slist0.index(data.iat[i, j]) + 1 + c - slist1.index(data.iat[i, j])) / 2
    print(R)
    return R

R=zzf(data,list)
n=R.shape[0]
p=R.shape[1]
W=[0.1537014472235063, 0.1514386808581634, 0.1622785796693402, 0.20715965902192388, 0.16296981482789508, 0.16245181839917122]
RSR=[]
WRSR=[]
for i in range(n):
    s=0
    ws=0
    for j in range(p):
        s=s+R.iat[i,j]
        ws=ws+R.iat[i,j]*W[j]
    RSR.append(s/n*p)
    WRSR.append(ws/n)
print(RSR)
print(WRSR)
RSR=pd.DataFrame({'RSR':RSR})
zzf(RSR,['RSR'])

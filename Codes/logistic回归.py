import pandas as pd
import os
import math

"""
本代码为logistic regression回归二分类模型，需要与spss结合使用，可以达到86%的准确性
使用时可以修改代码以贴合题目
https://zhuanlan.zhihu.com/p/74874291
"""

# file_path = os.path.join("data_2_标准化后数据.csv")
file_path = os.path.join("data1_标准化后_GB未.csv")
list=['id','PB','PS','NB','NS','KB','KS','W','UP','down','R','T','B']
data = pd.read_csv(open(file_path,'r',encoding='utf-8'),sep=',',usecols=list)
print(data)
def sig(PB,PS,NB,NS,KB,KS,W,UP,down,R,T):
    y=(math.exp(-5.967+87.306*PB+22.508*PS+2.766*NB+33.489*NS+19.438*KB-31.683*KS+0.852*UP+2.462*down+74.030*R+13.018*T))
    print(y)
    if (y/(y+1))>=0.5:
        return 1
    else:
        return 0
pre=[]
for i in range(0,123):
    x=sig(float(data.iat[i,1]),float(data.iat[i,2]),float(data.iat[i,3]),float(data.iat[i,4]),float(data.iat[i,5]),
              float(data.iat[i,6]),float(data.iat[i,7]),float(data.iat[i,8]),float(data.iat[i,9]),float(data.iat[i,10]),float(data.iat[i,11]))
    pre.append(x)
print(pre)
list_pre=['PB','PS','NB','NS','KB','KS','W','UP','down','R','T','B','preB']
data['preB']=pre
data.to_csv('test.csv', encoding='utf-8',index=False)
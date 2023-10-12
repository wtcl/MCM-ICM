# 问题1的大网络

import pandas as pd
import heapq
import math


edgeLinks = dict()
size = 0
stack = []

data=pd.read_csv("../data/influence_data.csv")
influencer=list(data['influencer_id'])
follower=list(data['follower_id'])

all_musician=list(set(influencer+follower))
print(all_musician)
print(len(all_musician))

data=pd.read_csv("../data/influence_data.csv")
influencerid=list(data['influencer_id'])
followerid=list(data['follower_id'])
all_musicianid=list(set(influencerid+followerid))
print(all_musicianid)


# 求解B流派因子
genre={}
for i in range(data.shape[0]):
    genre[str(data.iat[i,0])]=data.iat[i,2]
    genre[str(data.iat[i,4])]=data.iat[i,6]
B=[[math.inf for j in range(len(all_musicianid))] for i in range(len(all_musicianid))]
for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        if genre[str(all_musicianid[i])]==genre[str(all_musicianid[j])]:
            B[i][j]=0
        else:
            B[i][j]=1
print(B) # 获取了流派因子

T=[[0 for j in range(len(all_musicianid))] for i in range(len(all_musicianid))]
tt={}
for i in range(data.shape[0]):
    tt[str(data.iat[i,0])]=data.iat[i,3]
    tt[str(data.iat[i,4])]=data.iat[i,7]
def cal_t(a,b):
    if a>b:
        return (a-b)*2
    else:
        return b-a

for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        T[i][j]=cal_t(tt[str(all_musicianid[i])],tt[str(all_musicianid[j])])
print(T)  # 打印出时间


# 求解b间接影响
def addEdge(a,b):  #该函数进行加边操作   构造一个完整的字典形如
    '''edgeLinks{
  "1":["2" "5"]
  "2":["1" "3" "4"]
  "3":["2" "4" "5"]
  "4":["2" "3" "5"]
  "5":["1" "3" "4"]
  }'''
    global edgeLinks
    if a not in edgeLinks:
        edgeLinks[a] = set()
    if b not in edgeLinks:
        edgeLinks[b] = set()
    edgeLinks[a].add(b)  # 只加一条边，当作有向


def Check(graph, s, e, t):  # s起点，e终点
    # 存储所有路径
    n=(0.5**(5-t+1))*(1+B[all_musicianid.index(int(s))][all_musicianid.index(int(e))])*T[all_musicianid.index(int(s))][all_musicianid.index(int(e))]/160
    if t<0:
        return 0
    for node in graph[e]:
        ns = Check(graph, s, node, t-1)
        n=ns+n
    return n

def newCheck(graph, s):
    n=0
    for node in graph[s]:
       for node1 in graph[node]:
            n+=(0.5**2)*(1+B[all_musicianid.index(int(s))][all_musicianid.index(int(node1))])*T[all_musicianid.index(int(s))][all_musicianid.index(int(node1))]/160
       n+=(0.5)*(1+B[all_musicianid.index(int(s))][all_musicianid.index(int(node))])*T[all_musicianid.index(int(s))][all_musicianid.index(int(node))]/160
    return n

def load():  #读取文件并进行节点数边数，起点终点的获取
    f = open('newsample.txt', 'r') #需要把txt文件路径赋给左侧地址
    global size, edgeLinks
    size, edgeCount = map(int, f.readline().split())
    print("节点数为:%d"%size, "边数为:%d"%edgeCount)
    for i in range(edgeCount):
        a,b = f.readline().replace("\n",'').split(' ')
        addEdge(a,b)#进入addEdge函数 把边加进去 注意上面已经读过一行 还需要读取边数edgeCount行
        # print(a,b)

load()


A=[0 for j in range(len(all_musicianid))]
for i in range(len(all_musicianid)):
    A[i]=newCheck(edgeLinks,str(all_musicianid[i]))

print(A)  # 间接影响

# 权重W
W=[[math.inf for j in range(len(all_musician))] for i in range(len(all_musicianid))]
for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        if T[i][j]!=-1:
            W[i][j]=(1+B[i][j])*T[i][j]/160+A[j]
"""
D=[]
for i in range(len(all_musicianid)):
    t=0
    for j in range(len(all_musicianid)):
        if W[i][j]!=math.inf and str(all_musicianid[j]) in edgeLinks[str(all_musicianid[i])]:
            t+=W[i][j]
    D.append(t)
Ddata=pd.DataFrame({"id":all_musicianid,"D":D})
Ddata.to_csv("Ddata.csv",index=False)
"""

settable=[[],[]]
for i in range(data.shape[0]):
    if W[all_musicianid.index(data.iat[i,0])][all_musicianid.index(data.iat[i,4])]>100:
        settable[0].append(data.iat[i,0])
        settable[1].append(data.iat[i, 4])
side=pd.DataFrame({"source":settable[0],"target":settable[1]})
side.to_csv("side_data_fullnet.csv",index=False)
point=pd.DataFrame({"id":list(set(settable[0]+settable[1])),"lable":list(set(settable[0]+settable[1]))})
point.to_csv("point_data_fullnet.csv",index=False)

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

T=[[-1 for j in range(len(all_musician))] for i in range(len(all_musician))]
tt={}
for i in range(data.shape[0]):
    if data.iat[i,3]<data.iat[i,7]:
        tt[str(data.iat[i,0])+'-'+str(data.iat[i,4])]=2*(data.iat[i,7]-data.iat[i,3])
        tt[str(data.iat[i, 4]) +'-'+ str(data.iat[i, 0])] = (data.iat[i, 7] - data.iat[i, 3])
    else:
        tt[str(data.iat[i, 0]) +'-'+ str(data.iat[i, 4])] = (data.iat[i, 3] - data.iat[i, 7])
        tt[str(data.iat[i, 4]) + '-'+str(data.iat[i, 0])] = 2*(data.iat[i, 3] - data.iat[i, 7])
keys=tt.keys()
for i in range(len(all_musician)):
    for j in range(len(all_musician)):
        if str(all_musician[i])+'-'+str(all_musician[j]) in keys:
            T[i][j]=tt[str(all_musician[i])+'-'+str(all_musician[j])]
            print(T[i][j])
print(T)  # 打印出时间
# maxt=max(list(tt.values()))
# print(maxt)  # 160


"""
# 求解最小路径

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(s)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return distance

graph_dict = {
        # "A": {"B": 5, "C": 1},
        # "B": {"A": 5, "C": 2, "D": 1},
        # "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        # "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        # "E": {"C": 8, "D": 3},
        # "F": {"D": 6},
    }
for i in range(len(all_musician)):
    graph_dict[all_musician[i]]={}
for i in range(data.shape[0]):
    graph_dict[data.iat[i,1]][data.iat[i,5]]=1
biet=[]
for i in range(len(all_musician)):
    distance_dict = dijkstra(graph_dict, all_musician[i])
    biet.append(list(distance_dict.values()))
print(biet)
A=[[math.inf for i in range(len(all_musician))] for i in range(len(all_musician))]
for i in range(len(all_musician)):
    for j in range(len(all_musician)):
        if biet[i][j]!=math.inf:
            A[i][j]=0.5**biet[i][j]
print(A)  # 间接因子
"""

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

# 权重W
W=[[math.inf for j in range(len(all_musician))] for i in range(len(all_musicianid))]
for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        if T[i][j]!=-1:
            W[i][j]=(1+B[i][j])*T[i][j]/160+A[i][j]*(1+B[i][j])*T[i][j]/160
            print(W[i][j])

D=[]
for i in range(len(all_musicianid)):
    t=0
    for j in range(len(all_musicianid)):
        if W[i][j]!=math.inf:
            t+=W[i][j]
    D.append(t)
Ddata=pd.DataFrame({"id":all_musicianid,"D":D})
Ddata.to_csv("Ddata.csv",index=False)
import pandas as pd
import math
import heapq

edgeLinks = dict()
size = 0
stack = []

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


def Check(graph, s, e, t,path=[]):  # s起点，e终点

    # print('path',path)   取消注释查看当前path的元素
    if s == e:
        path = path + [s]
        # print('回溯')
        return [path]
    if t<=0:
        return []
    paths = []
    # 存储所有路径
    for node in graph[s]:
        if node not in path:
            path = path + [s]
            ns = Check(graph, node, e, t-1,path)
            if len(ns)==0:
                return []
            for n in ns:
                paths.append(n)
    # print(paths,'回溯')
    return paths


def load():  #读取文件并进行节点数边数，起点终点的获取
    f = open('newsample.txt', 'r') #需要把txt文件路径赋给左侧地址
    global size, edgeLinks
    size, edgeCount = map(int, f.readline().split())
    print("节点数为:%d"%size, "边数为:%d"%edgeCount)
    for i in range(edgeCount):
        a,b = f.readline().replace("\n",'').split(' ')
        addEdge(a,b)#进入addEdge函数 把边加进去 注意上面已经读过一行 还需要读取边数edgeCount行
        # print(a,b)

def findallway(a,b):
    # print("起点:", a, "终点:", b)
    allpath = Check(edgeLinks,a,b,5)
    t=0
    for p in allpath:
        # print(p)
        t=t+(len(p)-1)
    return t

load()
# print(edgeLinks)
data=pd.read_csv("../data/influence_data.csv")
influencerid=list(data['influencer_id'])
followerid=list(data['follower_id'])

all_musicianid=list(set(influencerid+followerid))
print(all_musicianid)
print(len(all_musicianid))


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

for i in range(len(all_musicianid)):
    graph_dict[all_musicianid[i]]={}
for i in range(data.shape[0]):
    graph_dict[data.iat[i,0]][data.iat[i,4]]=1
biet=[]
for i in range(len(all_musicianid)):
    distance_dict = dijkstra(graph_dict, all_musicianid[i])
    biet.append(list(distance_dict.values()))
print(biet)

b=[[0 for j in range(len(all_musicianid))] for i in range(len(all_musicianid))]
for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        if biet[i][j] and biet[i][j]!=math.inf:
            n=findallway(str(all_musicianid[i]),str(all_musicianid[j]))
            if n>=1:
                b[i][j]=n
                print(n)

for i in range(len(all_musicianid)):
    for j in range(len(all_musicianid)):
        if b[i][j]>0:
            b[i][j]=0.5**b[i][j]

print(b)
#!/usr/bin/env python3
from graphviz import Digraph

dot = Digraph(comment='Gragh2Print')
dot.edge_attr.update(arrowhead=True)
dot.graph_attr['rankdir'] = 'LR'

edgeLinks = dict()
size = 0

stack = []
nodeNumber = 0

def exitWithError(*error):
    print(*error)
    exit()

def printGraph2Pdf(grf): grf.render('graph-output/output.gv', view=True)

def printRoute(stackList):
    global nodeNumber
    nodeNumber += 1
    dot.node(str(nodeNumber), stackList[0])
    for node in stackList[1:]:
        nodeNumber += 1
        dot.node(str(nodeNumber), node)
        dot.edge(str(nodeNumber-1), str(nodeNumber))

def addEdge(a, b):
    global edgeLinks
    if a not in edgeLinks: edgeLinks[a] = set()
    if b not in edgeLinks: edgeLinks[b] = set()
    edgeLinks[a].add(b)
    edgeLinks[b].add(a)

def loadGraph(fileName="point_side.txt"):
    try: f = open(fileName, 'r')
    except: exitWithError("打开文件失败, 请检查文件名是否正确或程序是否有权限访问")
    global size, edgeLinks
    size, edgeCount = map(int, f.readline().split())
    print("节点:", size, "边数:", edgeCount)
    for i in range(1, size+1): dot.node(str(i), str(i))
    for i in range(edgeCount):
        a, b = f.readline().split()
        addEdge(a, b)
        dot.edge(a, b)
    re = f.readline()
    f.close()
    return re

def findAllRoutes(start, end):
    global edgeLinks, stack
    stack.append(start)
    if start == end:
        print("找到路径:", stack)
        printRoute(stack)
        stack.pop()
    else:
        for nextPoint in edgeLinks[start]:
            if nextPoint not in stack: findAllRoutes(nextPoint, end)
        stack.pop()

def rmRoute2Itself(start):
    for point in edgeLinks:
        if point != start and start in edgeLinks[point]:
            edgeLinks[point].remove(start)

if __name__ == '__main__':
    a, b = 1,2
    print("起点:", a, "终点:", b)
    rmRoute2Itself(a)
    nodeNumber = size + 1
    findAllRoutes(a, b)
    print("生成pdf格式图形化报告...")
    printGraph2Pdf(dot)

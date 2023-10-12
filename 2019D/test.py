import random
import math
import time
import numpy
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

start_time=time.time()

img_gray=np.zeros((10,10))

num=0
for i in range(2,8):
    for j in range(2,8):
        img_gray[i][j]=1

for i in range(3,6):
    for j in range(3,6):
        img_gray[i][j]=2

img_gray[3][2]=2
img_gray[4][2]=2
img_gray[7][6]=2
img_gray[7][7]=2
img_gray[5][2]=2
img_gray[7][5]=2

# 设置的内部的门通道
exit_door=[(3,2),(4,2),(7,6),(7,7)]
print(img_gray[3][2],img_gray[3][1])
print(img_gray[7][6],img_gray[8][6])


print(len(img_gray))
print(len(img_gray[0]))
door=exit_door

exit_door=list(set(exit_door+door))  # 包含出口的门和内部的门

dangerous=[(261,452)]   # 危险点

a,b,aaa,bbb,ccc,ddd=0.1,0.9,2,1,1,-1
max_distance=50

exit=np.zeros((10,10))
threat=np.zeros((10,10))
local_density=np.ones((10,10))/9
D=np.zeros((10,10))
N=np.zeros((10,10))
repel=np.ones((10,10))/25
attract=np.ones((10,10))/6
P=np.zeros((10,10))
W=np.zeros((10,10))

last_status=[np.zeros((10,10)),np.zeros((10,10))]

for i in range(len(img_gray)):
    for j in range(len(img_gray[i])):
        if img_gray[i][j]>0:
            min_door=[]
            for d in door:
                min_door.append((d[0]-j)**2+(d[1]-i)**2)
            exit[i][j]=1/(1+min(min_door))  # exit
            threat[i][j] = (math.sqrt((dangerous[0][1] - i) ** 2 + (dangerous[0][0] - j) ** 2))/max_distance  # threat

t=0

door_data={}
for ee in exit_door:
    door_data[str(ee)]=[]

numpy.savetxt(".//test//D{}.csv".format(str(t + 1)), D, delimiter=',')
numpy.savetxt(".//test//status{}.csv".format(str(t + 1)), img_gray, delimiter=',')

while t+1:
    t+=1
    print(t)
    if (last_status[-1]==img_gray).all() or (last_status[-2]==img_gray).all():  # 如果相邻两次都一样，就停
        break
    for ee in exit_door:   # 添加入门的状态
        door_data[str(ee)].append(img_gray[ee[0]][ee[1]])
    last_status.append(np.copy(img_gray))

    for i in range(len(img_gray)):   # 计算基础的量
        for j in range(len(img_gray[i])):
            if img_gray[i][j] > 0:
                min_door = []
                for d in door:
                    min_door.append((d[0] - j) ** 2 + (d[1] - i) ** 2)
                exit[i][j] = min(min_door) / max_distance
                threat[i][j] = 1 / (math.sqrt((dangerous[0][1] - i) ** 2 + (dangerous[0][0] - j) ** 2) + 1)
            elif img_gray[i][j] == 2 and i != 0 and i != 488 and j != 0 and j != 843:
                moore = [img_gray[i - 1][j - 1], img_gray[i - 1][j], img_gray[i - 1][j + 1],
                         img_gray[i][j - 1], img_gray[i][j + 1], img_gray[i + 1][j - 1]
                    , img_gray[i + 1][j], img_gray[i + 1][j + 1]]
                local_density[i][j] = (1 + moore.count(0) + moore.count(2)) / 9
                moore2 = [img_gray[i][j - 1], img_gray[i][j + 1], img_gray[i - 1][j], img_gray[i + 1][j]]
                moore3 = [img_gray[i - 1][j - 1], img_gray[i + 1][j + 1], img_gray[i - 1][j + 1],
                          img_gray[i + 1][j - 1]]
                repel[i][j] = ((moore2.count(0) + moore2.count(2)) + 0.5 * (moore3.count(0) + moore3.count(2))) / 6
            elif img_gray[i][
                j] == 2 and i != 0 and i != 1 and i != 487 and i != 488 and j != 0 and j != 1 and j != 843 and j != 842:
                moore1 = [img_gray[i - 1][j - 1], img_gray[i - 1][j], img_gray[i - 1][j + 1],
                          img_gray[i][j - 1], img_gray[i][j + 1], img_gray[i + 1][j - 1]
                    , img_gray[i + 1][j], img_gray[i + 1][j + 1], img_gray[i - 2][j - 2], img_gray[i - 2][j - 1],
                          img_gray[i - 2][j],
                          img_gray[i - 2][j + 1], img_gray[i - 2][j + 2], img_gray[i - 1][j - 2], img_gray[i][j - 2],
                          img_gray[i + 1][j - 2],
                          img_gray[i - 1][j + 2], img_gray[i][j + 2], img_gray[i + 1][j + 2], img_gray[i + 2][j - 2],
                          img_gray[i + 2][j - 1],
                          img_gray[i + 2][j], img_gray[i + 2][j + 1], img_gray[i + 2][j + 2]]
                attract[i][j] = (1 + moore1.count(0) + moore1.count(2)) / 25
            if img_gray[i][j] == 2:
                D[i][j] = (exit[i][j] * a + threat[i][j] * b) * local_density[i][j]
            # N[i][j] = math.exp(exit[i][j] * aaa + threat[i][j] * bbb + attract[i][j] * ccc + repel[i][j] * ddd)
            N[i][j] = math.exp(exit[i][j] * aaa + threat[i][j] * bbb)

    for out_door in exit_door:   # 将门口的人清除
        if img_gray[out_door[0]][out_door[1]] == 2:
            print(t,(out_door[0],out_door[1]))
            img_gray[out_door[0]][out_door[1]] = 1
    sample_img = np.copy(img_gray)
    for i in range(1, len(img_gray) - 1):
        for j in range(1, len(img_gray[i]) - 1):
            if sample_img[i][j] == 2:
                compare = {}  # 寻找4处的值
                compare[(i - 1, j)] = N[i - 1][j] * (1 - abs(img_gray[i - 1][j] - 1))
                compare[(i + 1, j)] = N[i + 1][j] * (1 - abs(img_gray[i + 1][j] - 1))
                compare[(i, j - 1)] = N[i][j - 1] * (1 - abs(img_gray[i][j - 1] - 1))
                compare[(i, j + 1)] = N[i][j + 1] * (1 - abs(img_gray[i][j + 1] - 1))
                compare = sorted(compare.items(), key=lambda d: d[1], reverse=True)  # 找最大的值
                # print(compare)
                if compare[0][1] > 0:
                    img_gray[compare[0][0][0]][compare[0][0][1]] = 2
                    img_gray[i][j] = 1

    numpy.savetxt(".//test//D{}.csv".format(str(t + 1)), D, delimiter=',')
    numpy.savetxt(".//test//status{}.csv".format(str(t + 1)), img_gray, delimiter=',')

newdoordata=pd.DataFrame(door_data)
newdoordata.to_csv(".//test//door.csv",index=False)
over_time=time.time()
print(over_time-start_time)

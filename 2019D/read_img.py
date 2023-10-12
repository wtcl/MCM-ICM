import random
import math
import time
import numpy
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

start_time=time.time()

imgdata=cv2.imread(".//0.png")

img = imgdata[:,:,(2,1,0)]
r,g,b = [img[:,:,i] for i in range(3)]
img_gray = r*0.299+g*0.587+b*0.114  # 灰度处理，将三维矩阵转为一维，即黑白图

num=0
for i in range(len(img_gray)):
    for j in range(len(img_gray[i])):
        if img_gray[i][j]==220.929:   # 墙和外面
            img_gray[i][j]=0
        else:
            img_gray[i][j]=1

site0=np.where(img_gray==1)

for i in range(len(site0[0])):
    try:
        if img_gray[site0[0][i]][site0[1][i]]==1 and img_gray[site0[0][i]-1][site0[1][i]]==1 and img_gray[site0[0][i]+1][site0[1][i]]==1 and img_gray[site0[0][i]][site0[1][i]-1]==1 and img_gray[site0[0][i]][site0[1][i]+1]==1 and random.randint(0,300)==0:
            img_gray[site0[0][i]][site0[1][i]]=2    # 设置人
            num+=1
    except:
        pass
# 加的所有障碍
for i in range(10,40):
    img_gray[i][73]=0
for i in range(50,78):
    img_gray[i][73] = 0
for i in range(426,450):
    img_gray[i][131]=0
for i in range(460,485):
    img_gray[i][131] = 0
for i in range(133,150):
    img_gray[i][570]=0
for i in range(160,186):
    img_gray[i][570] = 0
for i in range(334,350):
    img_gray[i][577]=0
for i in range(360,391):
    img_gray[i][577] = 0

# 设置的内部的门通道
exit_door=[]
for i in range(40,50):
    exit_door.append((i,73))
for i in range(450,460):
    exit_door.append((i,131))
for i in range(150,160):
    exit_door.append((i,570))
for i in range(350,360):
    exit_door.append((i,577))

print(num)
print(len(img_gray))
print(len(img_gray[0]))
# cv2.imshow('img',img_gray)
# k = cv2.waitKey(10000) & 0xff
# 出口的门
door=[]
for i in range(10,20):
    door.append((488,i))
for i in range(343,353):
    door.append((33,i))
for i in range(280,290):
    door.append(((343,i)))
for i in range(480,490):
    door.append((178,i))
for i in range(490,500):
    door.append((334,i))
for i in range(300,310):
    door.append((i,578))
for i in range(390,400):
    door.append((i,841))
# for d in door:
#     print(img_gray[d[0]][d[1]])
exit_door=exit_door+door  # 包含出口的门和内部的门

dangerous=[(261,452)]   # 危险点

a,b,aaa,bbb,ccc,ddd=0.1,0.9,2,1,1,-1

# max_distence=[]
# for i in range(len(img_gray)):
#     for j in range(len(img_gray[i])):
#         if img_gray[i][j]>0:
#             for k in door:
#                 max_distence.append((k[0]-j)**2+(k[1]-i)**2)
# print(math.sqrt(max(max_distence)))
max_distance=927

exit=np.zeros((489,844))
threat=np.zeros((489,844))
local_density=np.ones((489,844))/9
D=np.zeros((489,844))
N=np.zeros((489,844))
repel=np.ones((489,844))/25
attract=np.ones((489,844))/6
P=np.zeros((489,844))
W=np.zeros((489,844))

last_status=[np.zeros((489,844)),np.zeros((489,844))]

site1=np.where(img_gray>0)
for i in range(len(site1[0])):
    min_door = []
    for d in door:
        min_door.append((d[0] - site1[1][i]) ** 2 + (d[1] - site1[0][i]) ** 2)
    exit[site1[0][i]][site1[1][i]] = 1 / (1 + min(min_door))  # exit
    threat[site1[0][i]][site1[1][i]] = (math.sqrt((dangerous[0][1] - site1[0][i]) ** 2 + (dangerous[0][0] - site1[1][i]) ** 2)) / max_distance  # threat

t=0

door_data={}
for ee in exit_door:
    door_data[str(ee)]=[]

numpy.savetxt(".//data//D{}.csv".format(str(t + 1)), D, delimiter=',')
numpy.savetxt(".//data//status{}.csv".format(str(t + 1)), img_gray, delimiter=',')

while t+1:
    if (t+1)%100==0:  # 每100次存一下
        numpy.savetxt(".//data//D{}.csv".format(str(t+1)), D, delimiter=',')
        numpy.savetxt(".//data//status{}.csv".format(str(t+1)), img_gray, delimiter=',')
    t+=1

    print(t)

    if (last_status[-1]==img_gray).all() or (last_status[-2]==img_gray).all():  # 如果相邻两次都一样，就停
        break
    for ee in exit_door:   # 添加入门的状态
        door_data[str(ee)].append(img_gray[ee[0]][ee[1]])
    last_status.append(np.copy(img_gray))

    site2 =np.where(img_gray >0)
    for i in range(len(site2[0])):
        min_door = []
        for d in door:
            min_door.append((d[0] - site2[1][i]) ** 2 + (d[1] - site2[0][i]) ** 2)
        exit[site2[0][i]][site2[1][i]] = min(min_door) / max_distance
        threat[site2[0][i]][site2[1][i]] = 1 / (
                    math.sqrt((dangerous[0][1] - site2[0][i]) ** 2 + (dangerous[0][0] - site2[1][i]) ** 2) + 1)
        """
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
        """
        # if img_gray[i][j] == 2:
        # D[i][j] = (exit[i][j] * a + threat[i][j] * b) * local_density[i][j]
        # N[i][j] = math.exp(exit[i][j] * aaa + threat[i][j] * bbb + attract[i][j] * ccc + repel[i][j] * ddd)
        N[site2[0][i]][site2[1][i]] = math.exp(exit[site2[0][i]][site2[1][i]] * aaa + threat[site2[0][i]][site2[1][i]] * bbb)

    for out_door in exit_door:   # 将门口的人清除
        if img_gray[out_door[0]][out_door[1]] == 2:
            img_gray[out_door[0]][out_door[1]] = 1

    sample_img=np.copy(img_gray)
    site3 = np.where(img_gray ==2)
    for i in range(len(site3[0])):
        compare = {}  # 寻找4处的值
        compare[(site3[0][i] - 1, site3[1][i])] = N[site3[0][i] - 1][site3[1][i]] * (1 - abs(img_gray[site3[0][i] - 1][site3[1][i]] - 1))
        compare[(site3[0][i] + 1, site3[1][i])] = N[site3[0][i] + 1][site3[1][i]] * (1 - abs(img_gray[site3[0][i] + 1][site3[1][i]] - 1))
        compare[(site3[0][i], site3[1][i] - 1)] = N[site3[0][i]][site3[1][i] - 1] * (1 - abs(img_gray[site3[0][i]][site3[1][i] - 1] - 1))
        compare[(site3[0][i], site3[1][i] + 1)] = N[site3[0][i]][site3[1][i] + 1] * (1 - abs(img_gray[site3[0][i]][site3[1][i] + 1] - 1))
        compare = sorted(compare.items(), key=lambda d: d[1], reverse=True)  # 找最大的值
        # print(compare)
        if compare[0][1] > 0:
            img_gray[compare[0][0][0]][compare[0][0][1]] = 2
            img_gray[site3[0][i]][site3[1][i]] = 1

numpy.savetxt(".//data//D{}.csv".format(str(t + 1)), D, delimiter=',')
numpy.savetxt(".//data//status{}.csv".format(str(t + 1)), img_gray, delimiter=',')


newdoordata=pd.DataFrame(door_data)
newdoordata.to_csv("./data//door.csv",index=False)
over_time=time.time()
print(over_time-start_time)

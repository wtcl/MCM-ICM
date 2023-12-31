import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.random.randint(0,255,size=[40,40,40])
print(data)
x,y,z = data[0],data[1],data[2]
print(x[:10])
# print(y)
# print(z)
ax = plt.subplot(111,projection='3d')   #创建一个三维的绘图工程#将数据点分成三部分画,在颜色上有区分度
ax.scatter(x[ :10],y[ :10],z[ :10],c='y')   #绘制数据点
ax.scatter(x[ 10:20],y[10:20],z[10:20],c='r')
ax.scatter(x[30:40],y[30:40],z[30:40],c='g')
ax.set_zlabel('z')  #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

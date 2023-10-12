import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 绘图设置
fig = plt.figure()
ax = fig.gca(projection='3d')  # 三维坐标轴
# X和Y的个数要相同
X = [1,2,3,4,5]
Y = [1, 2, 3, 4, 5, 6, 7]
Z = [318.4704, 310.5654, 318.7775, 302.5342, 298.8752, 308.5907,
       306.0203, 265.7343, 269.3522, 265.4288, 245.0021, 254.9459,
       261.045 , 260.6406, 225.0952, 221.4523, 218.0884, 205.5786,
       224.3358, 219.5003, 223.2396, 190.6712, 174.6095, 174.1337,
       174.751 , 181.4198, 186.2276, 189.1521, 166.3381, 153.5574,
       153.2741, 153.8105, 159.0435, 162.7775, 165.0875]
# meshgrid把X和Y变成平方长度，比如原来都是4，经过meshgrid和ravel之后，长度都变成了16，因为网格点是16个
xx, yy = np.meshgrid(X, Y)  # 网格化坐标
X, Y = xx.ravel(), yy.ravel()  # 矩阵扁平化
print(X,Y)
# 设置柱子属性
height = np.zeros_like(Z)  # 新建全0数组，shape和Z相同，据说是图中底部的位置
width = depth = 0.3  # 柱子的长和宽
# 颜色数组，长度和Z一致
c = ['blue','red','yellow','green','orange']*7
# 开始画图，注意本来的顺序是X, Y, Z, width, depth, height，但是那样会导致不能形成柱子，只有柱子顶端薄片，所以Z和height要互换
ax.bar3d(X, Y, height, width, depth, Z, color=c, shade=False)  # width, depth, height
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
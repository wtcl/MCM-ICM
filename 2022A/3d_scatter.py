import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure() #创建画布
ax1 = plt.axes(projection = '3d') #创建三维的坐标系
xd = [65]*3+[75]*3+[85]*3
yd = [0.8,1,1.2]*3
zd = [338.279017906544,329.332570916414,303.811081446053,
      333.20032132046,310.565422605823,292.201688725393,
      326.239272816081,300.829375110352,286.943528353985]
zz=[159.742631105885,159.742631105885,159.742631105885,
153.557358960107,153.557358960107,153.557358960107,
148.300150513819,148.300150513819,148.300150513819
]

plt.xlabel('m')
plt.ylabel('a')  # 给坐标轴附上名字
ax1.scatter3D(xd,yd,zd,color = ['blue','yellow','orange']*3,marker='o') # 把xd,yd,zd放入绘制散点图
ax1.scatter3D(xd,yd,zz,color = ['red','green','pink']*3,marker='^')

plt.show()#展示出绘制出来的散点图
plt.show()

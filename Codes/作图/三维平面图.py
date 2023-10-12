from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
X= np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R= np.sqrt(X**2+Y**2)
z = np.sin(R)
# 具体函数方法可用help(function）查看，如:help(ax.plot_surface)
ax.plot_surface(X, Y,z,rstride=1, cstride=1,cmap='summer')
plt.show()

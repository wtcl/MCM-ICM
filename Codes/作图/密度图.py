import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ser = pd.Series(np.random.randn(1000))
# 多个样本数据
print(ser)
ser.plot.kde()
plt.show()
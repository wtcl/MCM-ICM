import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame(np.random.randn(5, 3),index=["a", "c", "e", "f", "h"],columns=["one", "two", "three"])
print(data)
data=pd.DataFrame(data)
data['four']=np.nan
print(data)
datanan=data.isin(data)  # 检查某一列是否含有空值，如果有，则对应位为false
print(datanan)
datanan2=data.notna()  # 同上检查，空值报错
print(datanan2)
data['five']=pd.Timestamp("20120101") # 表示日期
print(data)
datasum=data['one'].sum()  # 某一列求和
print(datasum)
# data['four'][0]=0.1
data.fillna(1) # 填充nan类型数据
print(data)
data.dropna()
print(data)
# data.plot() # 利用data画图
# plt.show()  # 展示
print(data.dtypes)
print(data.convert_dtypes().dtypes)
print(data)
print(data.index.is_unique) # 检查索引是否出现重复值
print(data.columns.is_unique) # 检查每一列是否出现重复值
print(data.loc[~data.index.duplicated(), :])  # 去除重复的标签
s = pd.Series(["a", "b", "c", "a"], dtype="category")
print(s)
data["five"] = data["one"].astype("category")  # 改变某一列数据类型
# print(data['one'].as_ordered) # 排序
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
plt.clf()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
df.plot()
plt.show()
print(data.cov())  #计算协方差矩阵
print(data.corr(method='pearson')) #计算pearson系数
print(data.corr(method='spearman')) #计算spearman系数
print(data.corr(method='kendall'))  #计算肯达尔系数
print(data['one'].mean()) #平均值
print(data['one'].std()) #标准差
print(data['one'].var()) #方差
print(data['one'].sem()) #均值的标准误差



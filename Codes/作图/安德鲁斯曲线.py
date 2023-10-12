from pandas.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt

# 此曲线主要为了观察数据是否呈现分类状况，如果曲线分离程度好，就是分类

data = pd.read_csv("data/iris.data")
andrews_curves(data, "Name")
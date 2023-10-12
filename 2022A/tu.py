import pandas as pd
import matplotlib.pyplot as plt

data1=pd.read_csv("1.csv")

a,ay=list(data1["x"]),list(data1["y"])
data2=pd.read_csv("2.csv")
b,by=list(data2["xx"]),list(data2["y"])
data3=pd.read_csv("3.csv")
c,cy=list(data3["xx"]),list(data3["y"])
data4=pd.read_csv("4.csv")
d,dy=list(data4["xx"]),list(data4["y"])
plt.fill_between(a,ay,color='red',alpha=0.4)
plt.fill_between(b,by,color='orange',alpha=0.4)
plt.fill_between(c,cy,color='green',alpha=0.4)
plt.fill_between(d,dy,color='blue',alpha=0.4)
plt.savefig("D://desktop//1.svg",dpi=1500)
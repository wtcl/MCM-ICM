import pandas as pd
import matplotlib.pyplot as plt

datatokyo=pd.read_csv("D://soft-project//MCM-ICM//2022A//tokyo.csv")

X=(list(datatokyo["X"]))
P=(list(datatokyo["P"]))

plt.plot(P,X)
plt.show()
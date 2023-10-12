import pandas as pd

data_influence=pd.read_csv("../q1/side_data_fullnet.csv")
id={}
for i in range(data_influence.shape[0]):
    if (data_influence.iat[i,0]) not in list(id.keys()):
        id[(data_influence.iat[i,0])]=0
    else:
        id[(data_influence.iat[i, 0])]+=1
id=sorted(id.items(),key=lambda x:x[1],reverse=True)
print(id)
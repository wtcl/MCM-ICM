import pandas as pd
import csv

"""
data=pd.read_csv("../data/influence_data.csv")
all_id=list(set(list(data['influencer_id'])+list(data['follower_id'])))
print(all_id)
print(len(all_id))


# 全部点的邻接矩阵
table=[[0 for j in range(len(all_id))] for i in range(len(all_id))]
for i in range(data.shape[0]):
    table[all_id.index(data.iat[i,0])][all_id.index(data.iat[i,4])]=1
print(table)
for i in range(len(all_id)):
    table[i]=[str(all_id[i])]+table[i]
table=[["id"]+all_id]+table
f = open('full_influence_table.csv','w',newline='')
writer = csv.writer(f)
for i in table:
    writer.writerow(i)
f.close()
"""
"""
Ddata=pd.read_csv("Ddata.csv")
dpoint={}
for i in range(Ddata.shape[0]):
    dpoint[Ddata.iat[i,0]]=Ddata.iat[i,1]
dpoint=sorted(dpoint.items(),key=lambda x:x[1],reverse=True)
choosed=[dpoint[n][0] for n in range(100)]
print(choosed)
table=[[0 for j in range(len(choosed))] for i in range(len(choosed))]
for i in range(data.shape[0]):
    if str(data.iat[i,0]) in choosed and str(data.iat[i,4]) in choosed:
        table[choosed.index(data.iat[i,0])][choosed.index(data.iat[i,4])]=1
print(table)
for i in range(len(choosed)):
    table[i]=[str(choosed[i])]+table[i]
table=[["id"]+choosed]+table
f = open('front100_table.csv','w',newline='')
writer = csv.writer(f)
for i in table:
    writer.writerow(i)
f.close()
"""

data=pd.read_csv("Ddata.csv")
data_inflence=pd.read_csv("../data/influence_data.csv")
name_id={}
for i in range(data_inflence.shape[0]):
    name_id[str(data_inflence.iat[i,0])]=data_inflence.iat[i,1]
    name_id[str(data_inflence.iat[i, 4])] = data_inflence.iat[i, 5]
name=[]
for i in range(data.shape[0]):
    name.append(name_id[str(data.iat[i,0])])
newdata=pd.DataFrame({"id":list(data['id']),"name":name,"点中心度":list(data['D'])})
newdata.to_csv("音乐家点中心度（影响力）.csv",index=False)
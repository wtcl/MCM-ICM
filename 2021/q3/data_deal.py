# 给full_music_data加上标签
import pandas as pd

data_influence=pd.read_csv("../data/influence_data.csv")
id_type={}
for i in range(data_influence.shape[0]):
    id_type['['+str(data_influence.iat[i,0])+']']=data_influence.iat[i,2]
    id_type['[' + str(data_influence.iat[i, 4]) + ']'] = data_influence.iat[i, 6]

data_full=pd.read_csv("../data/full_music_data.csv")
keys=list(id_type.keys())
print(keys)
newdata=[]
for key in range(len(keys)):
    newdata.append(data_full[data_full['artists_id']==keys[key]])
newdata=pd.concat(newdata,axis=0)
print(newdata)
type=[]
for i in range(newdata.shape[0]):
    type.append(id_type[newdata.iat[i,1]])
newdata.to_csv("newdata.csv",index=False)
finaldata=pd.DataFrame({"Type":type})
finaldata.to_csv("typefulldata.csv",index=False)
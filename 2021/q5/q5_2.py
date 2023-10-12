import pandas as pd
import numpy as np
import math

data_year=pd.read_csv("../data/data_by_year.csv", usecols=[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11])
data_year=(data_year[data_year['year']==1945])
del data_year['year']
print(data_year)
data_full=pd.read_csv("../data/full_music_data.csv", usecols=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 16])

data_full=data_full[data_full['year']==1946]
id=list(data_full['artists_id'])
del data_full['artists_id']
del data_full['year']
print(data_full)
newdata=pd.concat([data_year,data_full],ignore_index=False)
index_name=['danceability', 'energy', 'valence', 'tempo', 'loudness', 'key',
       'acousticness', 'instrumentalness', 'liveness', 'speechiness']
max_min_scaler = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))
for i in range(len(index_name)):
    newdata[index_name[i]]=newdata[[index_name[i]]].apply(max_min_scaler)
print(newdata)
newdata.to_csv("test.csv",index=False)

def cal_cos_star(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10):
    print(a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10)
    print(math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2))
    print(math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2))
    print('-----')
    return ((a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10)/
            (math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2)*
             math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2)))

similarity=[]
for i in range(1,newdata.shape[0]):
    similarity.append(cal_cos_star(
        newdata.iat[0,0],newdata.iat[0,1],newdata.iat[0,2],newdata.iat[0,3],
        newdata.iat[0,4],newdata.iat[0,5],newdata.iat[0,6],newdata.iat[0,7],
        newdata.iat[0, 8],newdata.iat[0,9],
        newdata.iat[i,0],newdata.iat[i,1],newdata.iat[i, 2],newdata.iat[i,3],
        newdata.iat[i, 4], newdata.iat[i, 5], newdata.iat[i, 6], newdata.iat[i, 7],
        newdata.iat[i, 8], newdata.iat[i, 9]
    ))
print(similarity)
data=pd.DataFrame({"id":id,"similarity":similarity})
data.to_csv("similarity.csv")
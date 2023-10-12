# long time
import pandas as pd
import numpy as np
import math

data_influence=pd.read_csv("../data/influence_data.csv")
followers={}
for i in range(data_influence.shape[0]):
    if data_influence.iat[i,0]==754032 and data_influence.iat[i,3]>data_influence.iat[i,7]:
        followers[str(data_influence.iat[i,4])]=data_influence.iat[i,7]
print(followers)
followers=list(followers.keys())
data_full=pd.read_csv("../data/full_music_data.csv")
tlist=[]
tlist.append(data_full[data_full['artists_id']=='[754032]'])
for i in range(len(followers)):
    tlist.append(data_full[data_full['artists_id']=='['+followers[i]+']'])
data_full=pd.concat(tlist,ignore_index=False)
print(data_full)

max_min_scaler = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))
data_full['danceability']=data_full[['danceability']].apply(max_min_scaler)
data_full['energy']=data_full[['energy']].apply(max_min_scaler)
data_full['valence']=data_full[['valence']].apply(max_min_scaler)
data_full['tempo']=data_full[['tempo']].apply(max_min_scaler)
data_full['loudness']=data_full[['loudness']].apply(max_min_scaler)
data_full['mode']=data_full[['mode']].apply(max_min_scaler)
data_full['key']=data_full[['key']].apply(max_min_scaler)
data_full['acousticness']=data_full[['acousticness']].apply(max_min_scaler)
data_full['instrumentalness']=data_full[['instrumentalness']].apply(max_min_scaler)
data_full['liveness']=data_full[['liveness']].apply(max_min_scaler)
data_full['speechiness']=data_full[['speechiness']].apply(max_min_scaler)
data_full['explicit']=data_full[['explicit']].apply(max_min_scaler)
print(data_full)
data_full.to_csv("full.csv",index=False)

def cal_cos_star(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12):
    return ((a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10+a11*b11+a12*b12)/
            (math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2+a11**2+a12**2)*
             math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2+b11**2+b12**2)))

data_infer=data_full[data_full['artists_id']=='[754032]']

similarity_data=[]
for ii in range(len(followers)):
    data_fulli=data_full[data_full['artists_id']==('['+followers[ii]+']')]
    newdata=data_fulli[data_fulli['year']>=1963]
    tdata=[]
    if newdata.empty!=True:
        for m in range(data_infer.shape[0]):
            for n in range(newdata.shape[0]):
                tdata.append(cal_cos_star(data_infer.iat[m,2],data_infer.iat[m,3],data_infer.iat[m,4],data_infer.iat[m,5]
                             ,data_infer.iat[m,6],data_infer.iat[m,7],data_infer.iat[m,8],data_infer.iat[m,9],
                             data_infer.iat[m,10],data_infer.iat[m,11],data_infer.iat[m,12],data_infer.iat[m,13],
                             newdata.iat[n, 2], newdata.iat[n, 3], newdata.iat[n, 4],newdata.iat[n, 5]
                             , newdata.iat[n, 6], newdata.iat[n, 7], newdata.iat[n, 8], newdata.iat[n, 9],
                             newdata.iat[n, 10], newdata.iat[n, 11], newdata.iat[n, 12], newdata.iat[n, 13],
                             ))
        similarity_data.append(sum(tdata)/len(tdata))
    else:
        similarity_data.append(0)
print(similarity_data)
exdata=pd.DataFrame({"id":followers,"similarity_data":similarity_data})
exdata.to_csv("754032_longtime_future.csv",index=False)

similarity_data=[]
for ii in range(len(followers)):
    data_fulli=data_full[data_full['artists_id']==('['+followers[ii]+']')]
    newdata=data_fulli[data_fulli['year']<1963]
    tdata=[]
    if newdata.empty!=True:
        for m in range(data_infer.shape[0]):
            for n in range(newdata.shape[0]):
                tdata.append(cal_cos_star(data_infer.iat[m,2],data_infer.iat[m,3],data_infer.iat[m,4],data_infer.iat[m,5]
                             ,data_infer.iat[m,6],data_infer.iat[m,7],data_infer.iat[m,8],data_infer.iat[m,9],
                             data_infer.iat[m,10],data_infer.iat[m,11],data_infer.iat[m,12],data_infer.iat[m,13],
                             newdata.iat[n, 2], newdata.iat[n, 3], newdata.iat[n, 4],newdata.iat[n, 5]
                             , newdata.iat[n, 6], newdata.iat[n, 7], newdata.iat[n, 8], newdata.iat[n, 9],
                             newdata.iat[n, 10], newdata.iat[n, 11], newdata.iat[n, 12], newdata.iat[n, 13],
                             ))
        similarity_data.append(sum(tdata)/len(tdata))
    else:
        similarity_data.append(0)
print(similarity_data)
exdata=pd.DataFrame({"id":followers,"similarity_data":similarity_data})
exdata.to_csv("754032_longtime_past.csv",index=False)

similarity_data=[]
for i in range(len(followers)):
    data_fulli=data_full[data_full['artists_id']==('['+followers[i]+']')]
    newdata0=data_fulli[data_fulli['year']>=1963]
    newdata1 = data_fulli[data_fulli['year']<1963]
    tdata=[]
    if newdata0.empty!=True and newdata1.empty!=True>0:
        for m in range(newdata0.shape[0]):
            for n in range(newdata1.shape[0]):
                tdata.append(cal_cos_star(
                            newdata0.iat[m, 2], newdata0.iat[m, 3], newdata0.iat[m, 4],newdata0.iat[m, 5]
                            ,newdata0.iat[m, 6], newdata0.iat[m, 7], newdata0.iat[m, 8], newdata0.iat[m, 9],
                            newdata0.iat[m, 10], newdata0.iat[m, 11], newdata0.iat[m, 12], newdata0.iat[m, 13],
                            newdata1.iat[n, 2], newdata1.iat[n, 3], newdata1.iat[n, 4], newdata1.iat[n, 5]
                            ,newdata1.iat[n, 6], newdata1.iat[n, 7], newdata1.iat[n, 8], newdata1.iat[n, 9],
                            newdata1.iat[n, 10], newdata1.iat[n, 11], newdata1.iat[n, 12],newdata1.iat[n, 13]
                             ))
        similarity_data.append(sum(tdata)/len(tdata))
    else:
        similarity_data.append(0)
print(similarity_data)
exdata=pd.DataFrame({"id":followers,"similarity_data":similarity_data})
exdata.to_csv("754032_followerself_longtime.csv",index=False)
# 圈2
import pandas as pd
import numpy as np
from collections import Counter

data_influence=pd.read_csv("../data/influence_data.csv")
followers={}
for i in range(data_influence.shape[0]):
    if data_influence.iat[i,0]==66915 and data_influence.iat[i,3]>data_influence.iat[i,7]:
        followers[str(data_influence.iat[i,4])]=data_influence.iat[i,7]
print(followers)
followers=list(followers.keys())

"""
data_full=pd.read_csv("../data/full_music_data.csv")
tlist=[]
tlist.append(data_full[data_full['artists_id']=='[66915]'])
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


def cal_cos_star(a,b):
    sub=[]
    for i in range(len(a)):
        sub.append(b[i]-a[i])
    # sub=sorted(sub.items(),key=lambda x:x[1],reverse=True)
    # return [sub[0][0],sub[1][0],sub[2][0]]
    return sub

data_infer=data_full[data_full['artists_id']=='[66915]']

similarity_data=[]
for ii in range(len(followers)):
    data_fulli=data_full[data_full['artists_id']==('['+followers[ii]+']')]
    newdata0=data_fulli[data_fulli['year']>=1963]
    tdata0=[0 for i in range(12)]
    if newdata0.empty!=True:
        for m in range(data_infer.shape[0]):
            for n in range(newdata0.shape[0]):
                t=cal_cos_star([data_infer.iat[m,2],data_infer.iat[m,3],data_infer.iat[m,4],data_infer.iat[m,5]
                             ,data_infer.iat[m,6],data_infer.iat[m,7],data_infer.iat[m,8],data_infer.iat[m,9],
                             data_infer.iat[m,10],data_infer.iat[m,11],data_infer.iat[m,12],data_infer.iat[m,13]],
                             [newdata0.iat[n, 2], newdata0.iat[n, 3], newdata0.iat[n, 4],newdata0.iat[n, 5]
                             , newdata0.iat[n, 6], newdata0.iat[n, 7], newdata0.iat[n, 8], newdata0.iat[n, 9],
                             newdata0.iat[n, 10], newdata0.iat[n, 11], newdata0.iat[n, 12], newdata0.iat[n, 13]]
                             )
                tdata0=[tdata0[i] + t[i] for i in range(min(len(tdata0), len(t)))]
        tdata0=[infer /(data_infer.shape[0]*newdata0.shape[0]) for infer in tdata0]
    newdata1 = data_fulli[data_fulli['year'] < 1963]
    tdata1 = [0 for i in range(12)]
    if newdata1.empty != True:
        for m in range(data_infer.shape[0]):
            for n in range(newdata1.shape[0]):
                t = cal_cos_star([data_infer.iat[m, 2], data_infer.iat[m, 3], data_infer.iat[m, 4], data_infer.iat[m, 5]
                                     , data_infer.iat[m, 6], data_infer.iat[m, 7], data_infer.iat[m, 8],
                                  data_infer.iat[m, 9],
                                  data_infer.iat[m, 10], data_infer.iat[m, 11], data_infer.iat[m, 12],
                                  data_infer.iat[m, 13]],
                                 [newdata1.iat[n, 2], newdata1.iat[n, 3], newdata1.iat[n, 4], newdata1.iat[n, 5]
                                     , newdata1.iat[n, 6], newdata1.iat[n, 7], newdata1.iat[n, 8], newdata1.iat[n, 9],
                                  newdata1.iat[n, 10], newdata1.iat[n, 11], newdata1.iat[n, 12], newdata1.iat[n, 13]]
                                 )
                tdata1 = [tdata1[i] + t[i] for i in range(min(len(tdata1), len(t)))]
        tdata1 = [infer / (data_infer.shape[0] * newdata1.shape[0]) for infer in tdata1]
    print(tdata1)
    print(tdata0)
    if sum(tdata0)!=0 and sum(tdata1)!=0:
        tdata0 = [(tdata1[i] - tdata0[i]) / tdata0[i] for i in range(min(len(tdata0), len(tdata1)))]
        d = tdata0[::]
        d = sorted(d, reverse=True)
        similarity_data.append([tdata0.index(d[0]), tdata0.index(d[1]), tdata0.index(d[2])])
    else:
        similarity_data.append([])
print(similarity_data)

# exdata=pd.DataFrame({"id":followers,"similarity_data":similarity_data})
# exdata.to_csv("66915_longtime_future.csv",index=False)
#
# similarity_data=[]
# for ii in range(len(followers)):
#     data_fulli=data_full[data_full['artists_id']==('['+followers[ii]+']')]
#     newdata=data_fulli[data_fulli['year']<1963]
#     tdata=[0 for i in range(12)]
#     if newdata.empty!=True:
#         for m in range(data_infer.shape[0]):
#             for n in range(newdata.shape[0]):
#                 t=cal_cos_star([data_infer.iat[m,2],data_infer.iat[m,3],data_infer.iat[m,4],data_infer.iat[m,5]
#                              ,data_infer.iat[m,6],data_infer.iat[m,7],data_infer.iat[m,8],data_infer.iat[m,9],
#                              data_infer.iat[m,10],data_infer.iat[m,11],data_infer.iat[m,12],data_infer.iat[m,13]],
#                              [newdata.iat[n, 2], newdata.iat[n, 3], newdata.iat[n, 4],newdata.iat[n, 5]
#                              , newdata.iat[n, 6], newdata.iat[n, 7], newdata.iat[n, 8], newdata.iat[n, 9],
#                              newdata.iat[n, 10], newdata.iat[n, 11], newdata.iat[n, 12], newdata.iat[n, 13]]
#                              )
#                 tdata=[tdata[i] + t[i] for i in range(min(len(tdata), len(t)))]
#         d = tdata[::]
#         d=sorted(d,reverse=True)
#         similarity_data.append([tdata.index(d[0]),tdata.index(d[1]),tdata.index(d[2])])
#     else:
#         similarity_data.append([])
# print(similarity_data)
"""
type=[[], [], [9, 5, 10], [], [5, 7, 9], [10, 3, 9], [], [], [], [], [], [6, 2, 5], [], [0, 8, 5], [], [9, 7, 1], [], [6, 9, 7], [], [3, 9, 0], [], []]
ty=['danceability',
 'energy',
 'valence',
 'tempo',
 'loudness',
 'mode',
 'key',
 'acousticness',
 'instrumentalness',
 'liveness',
 'speechiness',
 'explicit']
a=[]
b=[]
c=[]
id=[]
for f in range(len(followers)):
    if len(type[f])>0:
        id.append(followers[f])
        a.append(ty[type[f][0]])
        b.append(ty[type[f][1]])
        c.append(ty[type[f][2]])
data=pd.DataFrame({"id":id,"type_a":a,"type_b":b,"type_c":c})
data.to_csv("66915_id_type.csv",index=False)
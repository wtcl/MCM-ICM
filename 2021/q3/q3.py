import itertools

import pandas as pd
import math
import csv


data_full=pd.read_csv("../data/full_music_data.csv")
data_influence=pd.read_csv("../data/influence_data.csv")
"""
id_type={}
for i in range(data_influence.shape[0]):
    id_type['['+str(data_influence.iat[i,0])+']']=data_influence.iat[i,2]
    id_type['[' + str(data_influence.iat[i, 4]) + ']'] = data_influence.iat[i, 6]
dataD=pd.read_csv("../q1/Ddata.csv")
id_D={}
for i in range(dataD.shape[0]):
    id_D['['+str(dataD.iat[i,0])+']']=dataD.iat[i,1]
dataD=sorted(id_D.items(),key=lambda x:x[1],reverse=True)
popdata=[]
for i in dataD:
    if id_type[i[0]]=='Pop/Rock':
        popdata.append(i[0])
popdata=popdata[:20]
print(popdata)
"""
chooseid=['[754032]', '[66915]', '[120521]', '[824022]', '[894465]', '[180228]', '[354105]', '[55128]', '[538677]', '[100160]', '[577627]', '[840402]', '[489303]', '[332141]', '[46699]', '[41874]', '[562304]', '[631774]', '[531986]', '[112462]']
"""
id_year={}
for i in range(data_influence.shape[0]):
    id_year['['+str(data_influence.iat[i,0])+']']=data_influence.iat[i,3]
    id_year['[' + str(data_influence.iat[i, 4]) + ']'] = data_influence.iat[i, 7]
years=[]
for i in range(len(chooseid)):
    years.append(id_year[chooseid[i]])
print(years)
"""
years=[1960, 1960, 1950, 1950, 1960, 1950, 1960, 1940, 1950, 1960, 1960, 1960, 1960, 1950, 1950, 1960, 1960, 1960, 1960, 1960]


def guione(a):
    return [(i-min(a))/(max(a)-min(a)) for i in a]
    
def cal_cos_star(a1,a2,a3,b1,b2,b3):
    return ((a1*b1+a2*b2+a3*b3)/
            (math.sqrt(a1**2+a2**2+a3**2)*
             math.sqrt(b1**2+b2**2+b3**2)))

data_artist=pd.read_csv("../data/data_by_artist.csv")
data=[]
for i in range(len(chooseid)):
    data.append(data_artist[data_artist['artist_id']==int(chooseid[i].replace("[",'').replace("]",''))])
data_artist=pd.concat(data,ignore_index=False)
print(data_artist)
data_artist.to_csv("test.csv")
artistid=list((data_artist['artist_id']))
artist_danceability=guione(list(data_artist['danceability']))
artist_acousticness=guione(list(data_artist['acousticness']))
artist_instrumentalness=guione(list(data_artist['instrumentalness']))
artist_liveness=guione(list(data_artist['liveness']))
artist_speechiness=guione((list(data_artist['speechiness'])))
# artist_explicit=guione(list(data_artist['explicit']))
artist_energy=guione((list(data_artist['energy'])))
artist_valence=guione(list(data_artist['valence']))
artist_tempo=guione(list(data_artist['tempo']))
artist_loudness=guione(list(data_artist['loudness']))
# artist_mode=guione(list(data_artist['mode']))
artist_key=guione(list(data_artist['key']))

# 原始的
all_symbol=[artist_danceability,artist_acousticness,artist_instrumentalness,artist_liveness,artist_speechiness,artist_energy,artist_valence,artist_tempo,artist_loudness,artist_key]
cosa={}
for sample in itertools.combinations(all_symbol,4):
    n=0
    try:
        for i in range(len(artistid)):
            for j in range(len(artistid)):
                n+= cal_cos_star(sample[0][i],sample[1][i],sample[2][i],sample[0][j],sample[1][j],sample[2][j])
        cosa[str(all_symbol.index(sample[0])) + str(all_symbol.index(sample[1])) + str(all_symbol.index(sample[2]))] = n
    except:
        continue
print(sorted(cosa.items(),key=lambda x:x[1],reverse=True))

# choose_char=[artist_energy,artist_tempo,artist_loudness]
"""
print(cosa)
f = open('cosa0.csv','w',newline='')
writer = csv.writer(f)
for i in cosa:
    writer.writerow(i)
f.close()

"""
"""
# 新的

data_year=pd.read_csv("../data/data_by_year.csv")

table_sub=[]
for name in chooseid:
    table_sub.append(data_full[(data_full['artists_id'])==('['+str(name)+']')])
for i in range(1,9):
    table_sub[0]=table_sub[0].append(table_sub[i],ignore_index=True)
data_s=(table_sub[0])
a_id=list(data_s['artists_id'])
a_danceability = list(data_s['danceability'])
a_acousticness = list(data_s['acousticness'])
a_instrumentalness = list(data_s['instrumentalness'])
a_liveness = list(data_s['liveness'])
a_speechiness=list(data_s['speechiness'])
# a_explicit=list(data_s['explicit'])
a_energy=list(data_s['energy'])
a_valence=list(data_s['valence'])
a_tempo=list(data_s['tempo'])
a_loudness=list(data_s['loudness'])
a_mode=list(data_s['mode'])
a_key=list(data_s['key'])
for i in range(data_s.shape[0]):
    if int(a_id[i].replace("[",'').replace("]",'')) in years:
        a_danceability[i]=a_danceability[i]-data_year[data_year['year']==int(a_id[i].replace("[",'').replace("]"))].iat[i,1]
        a_acousticness[i] = a_acousticness[i]-data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 8]
        a_instrumentalness[i] = a_instrumentalness[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 9]
        a_liveness[i] = a_liveness[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 10]
        a_speechiness[i] = a_speechiness[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 11]
        a_energy[i] = a_energy[i] -data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 2]
        a_valence[i] = a_valence[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 3]
        a_tempo[i] = a_tempo[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 4]
        a_loudness[i] = a_loudness[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 5]
        a_mode[i] = a_mode[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 6]
        a_key[i] = a_key[i] - data_year[data_year['year'] == int(a_id[i].replace("[", '').replace("]"))].iat[i, 7]

a_danceability = guione(data_s['danceability'])
a_acousticness = guione(data_s['acousticness'])
a_instrumentalness = guione(data_s['instrumentalness'])
a_liveness = guione(data_s['liveness'])
a_speechiness=guione(data_s['speechiness'])
# a_explicit=guione(data_s['explicit'])
a_energy=guione(data_s['energy'])
a_valence=guione(data_s['valence'])
a_tempo=guione(data_s['tempo'])
a_loudness=guione(data_s['loudness'])
a_mode=guione(data_s['mode'])
a_key=guione(data_s['key'])

art_data=pd.DataFrame({"id":a_id,"danceability":a_danceability,"acousticness":a_acousticness,"a_instrumentalness":a_instrumentalness,"liveness":a_liveness,
                       "a_speechiness":a_speechiness,"a_energy":a_energy,"a_valence":a_valence,"a_tempo":a_tempo,
                       "a_loudness":a_loudness,"a_mode":a_mode,"a_key":a_key})

print(art_data)
art_data.to_csv("art_data.csv",index=False)

cosa1=[[0 for j in range(len(chooseid))] for i in range(len(chooseid))]
for i in range(len(chooseid)):
    for j in range(len(chooseid)):
        data1=art_data[art_data['id']==('['+str(chooseid[i])+']')]
        data2 = art_data[art_data['id'] == ('[' + str(chooseid[j]) + ']')]
        t=0
        for k in range(data1.shape[0]):
            for l in range(data2.shape[0]):
                t+=cal_cos_star(data1.iat[k,1],data1.iat[k,2],data1.iat[k,3],data1.iat[k,4],
                                data1.iat[k, 5], data1.iat[k, 6], data1.iat[k, 7], data1.iat[k, 8],
                                data1.iat[k, 9], data1.iat[k, 10], data1.iat[k, 11],
                                data2.iat[l,1],data2.iat[l,2],data2.iat[l,3],data2.iat[l,4],
                                data2.iat[l, 5], data2.iat[l, 6], data2.iat[l, 7], data2.iat[l, 8],
                                data2.iat[l, 9], data2.iat[l, 10], data2.iat[l, 11])
        t=t/(data1.shape[0]*data2.shape[0])
        cosa1[i][j]=t
print(cosa1)


f = open('cosa1.csv','w',newline='')
writer = csv.writer(f)
for i in cosa1:
    writer.writerow(i)
f.close()
"""

"""
aver_max_min=[[],[],[]]
for k in range(1,4):
    t = []
    for i in range(3*(k-1),3*k):
        for j in range(3*(k-1),3*k):
            t.append(cosa[i][j])
    aver_max_min[0].append(sum(t)/9)
    aver_max_min[1].append(max(t))
    aver_max_min[2].append(min(t))
f = open('cosa0_same.csv','w',newline='')
writer = csv.writer(f)
for i in aver_max_min:
    writer.writerow(i)
f.close()

aver_max_min1=[[],[],[]]
mmmm=[[0,1,2],[3,4,5],[6,7,8]]
for k in range(1,4):
    t = []
    for i in mmmm[k]:
        for j in [i for i in range(9)]-mmmm[k]:
            t.append(cosa1[i][j])
    aver_max_min1[0].append(sum(t)/9)
    aver_max_min1[1].append(max(t))
    aver_max_min1[2].append(min(t))
f = open('cosa0_diff.csv','w',newline='')
writer = csv.writer(f)
for i in aver_max_min1:
    writer.writerow(i)
f.close()
"""
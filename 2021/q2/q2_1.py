import pandas as pd
import math
import csv

"""
data_full=pd.read_csv("../data/full_music_data.csv")
# ['artist_names', 'artists_id', 'danceability', 'energy', 'valence',
#        'tempo', 'loudness', 'mode', 'key', 'acousticness', 'instrumentalness',
#        'liveness', 'speechiness', 'explicit', 'duration_ms', 'popularity',
#        'year', 'release_date', 'song_title (censored)']
# Ddata=pd.read_csv("../q1/Ddata.csv")

# chooseid={"Pop/rock":[754032,66915,120521],"R&B;":[128099,46861,238115],"Jazz":[287604,317093,423829]}
def cal_cos_star(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11):
    return ((a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10+a11*b11)/
            (math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2+a11**2)*
             math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2+b11**2)))

chooseid=[754032,66915,824022,343396,46861,238115,259529,317093,423829]
years=[1960,1960,1950,1940,1940,1950,1930,1930,1940]

data_artist=pd.read_csv("./data_artist.csv")

def guione(a):
    return [(i-min(a))/(max(a)-min(a)) for i in a]

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
artist_mode=guione(list(data_artist['mode']))
artist_key=guione(list(data_artist['key']))

# 原始的
cosa=[[0 for j in range(len(artistid))] for i in range(len(artistid))]
for i in range(len(artistid)):
    for j in range(len(artistid)):
        cosa[i][j]=cal_cos_star(artist_danceability[i],artist_acousticness[i],artist_instrumentalness[i],artist_liveness[i],
                                artist_speechiness[i],artist_energy[i],
                                artist_valence[i],artist_tempo[i],artist_loudness[i],artist_mode[i],artist_key[i],
                                artist_danceability[j], artist_acousticness[j], artist_instrumentalness[j],artist_liveness[j],
                                artist_speechiness[j], artist_energy[j],
                                artist_valence[j], artist_tempo[j], artist_loudness[j], artist_mode[j], artist_key[j]
                                )

print(cosa)
f = open('cosa0.csv','w',newline='')
writer = csv.writer(f)
for i in cosa:
    writer.writerow(i)
f.close()

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


cosa=[]
with open("./cosa0.csv",'r',encoding='utf-8') as f:
    con=csv.reader(f)
    for i in con:
        cosa.append([float(k) for k in i])
print(cosa)

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
"""

cosa1=[]
with open("cosa1.csv", 'r', encoding='utf-8') as f:
    con=csv.reader(f)
    for i in con:
        cosa1.append([float(k) for k in i])
print(cosa1)

aver_max_min1=[[],[],[]]
mmmm=[[0,1,2],[3,4,5],[6,7,8]]

t = []
for i in mmmm[0]:
    for j in mmmm[1]:
        t.append(cosa1[i][j])
aver_max_min1[0].append(sum(t)/9)
aver_max_min1[1].append(max(t))
aver_max_min1[2].append(min(t))
t = []
for i in mmmm[0]:
    for j in mmmm[2]:
        t.append(cosa1[i][j])
aver_max_min1[0].append(sum(t)/9)
aver_max_min1[1].append(max(t))
aver_max_min1[2].append(min(t))
f = open('cosa1_diff.csv', 'w', newline='')
writer = csv.writer(f)
for i in aver_max_min1:
    writer.writerow(i)
f.close()



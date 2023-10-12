# 针对Jazz
import itertools
import pandas as pd
import math
import csv

data_full = pd.read_csv("../data/full_music_data.csv")
data_influence = pd.read_csv("../data/influence_data.csv")


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
    if id_type[i[0]]=='Jazz':
        popdata.append(i[0])
popdata=popdata[:20]
print(popdata)
chooseid=['[287604]', '[317093]', '[423829]', '[259529]', '[162677]', '[532957]', '[175553]', '[211758]', '[490416]', '[805930]', '[170690]', '[924232]', '[927627]', '[484396]', '[646353]', '[346637]', '[359199]', '[950571]', '[225389]', '[172350]']
def guione(a):
    return [(i - min(a)) / (max(a) - min(a)) for i in a]


def cal_cos_star(a1, a2, a3, b1, b2, b3):
    return ((a1 * b1 + a2 * b2 + a3 * b3) /
            (math.sqrt(a1 ** 2 + a2 ** 2 + a3 ** 2) *
             math.sqrt(b1 ** 2 + b2 ** 2 + b3 ** 2)))


data_artist = pd.read_csv("../data/data_by_artist.csv")
data = []
for i in range(len(chooseid)):
    data.append(data_artist[data_artist['artist_id'] == int(chooseid[i].replace("[", '').replace("]", ''))])
data_artist = pd.concat(data, ignore_index=False)
print(data_artist)
artistid = list((data_artist['artist_id']))
artist_danceability = guione(list(data_artist['danceability']))
artist_acousticness = guione(list(data_artist['acousticness']))
artist_instrumentalness = guione(list(data_artist['instrumentalness']))
artist_liveness = guione(list(data_artist['liveness']))
artist_speechiness = guione((list(data_artist['speechiness'])))
# artist_explicit=guione(list(data_artist['explicit']))
artist_energy = guione((list(data_artist['energy'])))
artist_valence = guione(list(data_artist['valence']))
artist_tempo = guione(list(data_artist['tempo']))
artist_loudness = guione(list(data_artist['loudness']))
# artist_mode=guione(list(data_artist['mode']))
artist_key = guione(list(data_artist['key']))

# 原始的
all_symbol = [artist_danceability, artist_acousticness, artist_instrumentalness, artist_liveness, artist_speechiness,
              artist_energy, artist_valence, artist_tempo, artist_loudness, artist_key]
cosa = {}
for sample in itertools.combinations(all_symbol, 4):
    n = 0
    try:
        for i in range(len(artistid)):
            for j in range(len(artistid)):
                n += cal_cos_star(sample[0][i], sample[1][i], sample[2][i], sample[3][i], sample[0][j], sample[1][j])
        cosa[str(all_symbol.index(sample[0])) + str(all_symbol.index(sample[1])) + str(all_symbol.index(sample[2]))] = n
    except:
        continue
print(sorted(cosa.items(), key=lambda x: x[1], reverse=True))
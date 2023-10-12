import math
import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber

tb = Blobber(analyzer=NaiveBayesAnalyzer())
data = pd.read_csv("../data//microwave.csv")

max_length=0
for i in range(data.shape[0]):
    l=math.log(len(data.iat[i, 12] + ' ' + data.iat[i, 13]))
    if max_length<l:
        max_length=l

E = []
S = []
L = []
C = []
for i in range(data.shape[0]):
    e, s = TextBlob(data.iat[i, 12] + ' ' + data.iat[i, 13]).sentiment
    if e==0:
        e = (tb(data.iat[i, 12] + ' ' + data.iat[i, 13]).sentiment.p_pos-0.5)/0.5
    E.append(e)
    S.append(s)
    L.append(len(data.iat[i, 12] + ' ' + data.iat[i, 13]))
    if e == 0:
        C.append(math.log(len(data.iat[i, 12] + ' ' + data.iat[i, 13]))/max_length)
    elif e < 0:
        C.append(-((-e) ** s) * math.log(len(data.iat[i, 12] + ' ' + data.iat[i, 13]))/max_length)
    else:
        C.append((e ** s) * math.log(len(data.iat[i, 12] + ' ' + data.iat[i, 13]))/max_length)

ev = []
num_encode = {'vine': {'Y': 2, 'y': 2, 'n': 1, 'N': 1},
              'verified_purchase': {'Y': 1, "y": 1, 'n': 0.1, 'N': 0.1},
              'star_rating':{1:-1,2:-0.6,3:-0.2,4:0.6,5:1}
              }
data.replace(num_encode, inplace=True)
for i in range(data.shape[0]):
    if data.iat[i, 9] > 0 and data.iat[i, 8] > 0:
        votes = data.iat[i, 9] ** (data.iat[i, 8] / data.iat[i, 9] - 0.5)
    else:
        votes = 1
    ev.append(votes * data.iat[i, 11] * data.iat[i, 10] * data.iat[i, 7])

data["E"]=E
data["S"]=S
data["L"]=L
data["C"]=C
data["evaluation"]=ev

data.to_csv("./CE_venter_microwave.csv",index=False)


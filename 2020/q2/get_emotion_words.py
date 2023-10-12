import pandas as pd
import jieba
from textblob import TextBlob

data=pd.read_csv("../data/hair_dryer.csv")

pos=[]
nag=[]
for i in range(data.shape[0]):
    t=jieba.lcut(data.iat[i,12]+' '+data.iat[i,13])
    t=list(set(t))
    for text in t:
        if TextBlob(text).sentiment[0]>0.5:
            pos.append(text)
        elif TextBlob(text).sentiment[0]<-0.5:
            nag.append(text)
print(list(set(pos)))
print(list(set(nag)))
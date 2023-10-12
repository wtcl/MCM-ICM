import pandas as pd
from textblob import TextBlob

data0=pd.read_csv("../data/pacifier.csv",usecols=["star_rating","helpful_votes","total_votes","vine","verified_purchase","review_headline","review_body"])

emo=[]
sub=[]
long=[]

for i in range(data0.shape[0]):
    review=data0.iat[i,5]+" "+data0.iat[i,6]
    emo.append(TextBlob(review).sentiment[0])
    sub.append(TextBlob(review).sentiment[1])
    long.append(len(review))
data0["emo"]=emo
data0["sub"]=sub
data0["long"]=long
del data0["review_headline"]
del data0["review_body"]
num_encode = {'vine' : {'Y':1,'y':1,'n':0, 'N':0},
                  'verified_purchase'  : {'Y':1, "y":1,'n':0, 'N':0}}
data0.replace(num_encode, inplace=True)
data0 = (data0-data0.min())/(data0.max()-data0.min())
# print(set(list(data0["vine"])))
# print(set(list(data0["verified_purchase"])))
# print(set(list(data0["long"])))
result=data0.corr(method='pearson')
result.to_csv("pacifier_pearson.csv",index=False)
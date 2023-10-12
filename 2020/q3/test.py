import pandas as pd
from textblob import Blobber,TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

tb=Blobber(analyzer=NaiveBayesAnalyzer())
data=pd.read_csv("../data//hair_dryer.csv")

data=data[data['product_parent']==732252283]
data['review_date'] = pd.to_datetime(data['review_date'], format="%m/%d/%Y")
data.sort_values("review_date",inplace=True)

emotion=[]
for i in range(data.shape[0]):
    emotion.append((TextBlob(data.iat[i,13]+' '+data.iat[i,12]).sentiment[0]+1))
newdata=pd.DataFrame({"star":list(data['star_rating']),"emotion":emotion})
print(newdata.corr(method='spearman'))
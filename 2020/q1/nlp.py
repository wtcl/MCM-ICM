from textblob import TextBlob
import pandas as pd
# import pretty_errors

# text = "I am happy today. I feel sad today."
# t="Recently found out my best friend is the same & she (like me) was convinced there was no way around it.  Writing this review b/c there's probably more of us out there.  And you 100% aren't stuck."
# blob = TextBlob(t)
# print(blob.sentiment[1])
#
data0=pd.read_csv("../data/hair_dryer.csv")
# data1=pd.read_csv("../data/microwave.csv")
# data2=pd.read_csv("../data/pacifier.csv")
#
# data_grade=[]
# for i in range(1,6):
#     data_grade.append(data0[data0["star_rating"]==i].reset_index(drop=True))
# print(data_grade)

for i in range(data0.shape[0]):
    with open(str(data0.iat[i,7])+".txt",'a',encoding='utf-8') as f:
        f.write(data0.iat[i,12]+' '+data0.iat[i,13]+'\n')
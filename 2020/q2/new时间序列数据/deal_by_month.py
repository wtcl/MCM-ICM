import pandas as pd
import datetime

data=pd.read_csv("./732252283.csv")
for i in range(data.shape[0]):
    data.iat[i,14]=datetime.datetime.strftime(pd.to_datetime(data.iat[i,14]), "%Y-%m")
m=list(set((data['review_date'])))
wdata=[]
for mon in m:
    ndata=data[data['review_date']==mon]
    wdata.append(sum(list(ndata['Wdata'])))
print(wdata)
newdata=pd.DataFrame({"month":m,"wdata":wdata})
newdata.to_csv("new_732252283.csv",index=False)
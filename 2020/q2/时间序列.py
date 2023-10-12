import pandas as pd
from datetime import datetime
import time

data=pd.read_csv("./CE_venter_microwave.csv")
data['review_date'] = pd.to_datetime(data['review_date'], format="%m/%d/%Y")
data.sort_values("review_date",inplace=True)
data=data[data['product_parent']==423421857]

print(data.iat[0,14])
print(data.iat[-1,14])
print(data.shape[0])

ndata=data
ndata.index = [i for i in range(ndata.shape[0])]
maxtime = (ndata.iat[-1, 14].date() - ndata.iat[0, 14].date()).days
print(maxtime)
wdata = []
result=[]
for i in range(ndata.shape[0]):
    t = ndata.iat[i, 14].date()
    if ndata.iat[i, 18] < 0 and ndata.iat[i, 19] < 0:
        wdata.append(-ndata.iat[i, 18] * ndata.iat[i, 19] * (1 - (ndata.iat[-1,14].date() - t).days / maxtime))
    else:
        wdata.append(ndata.iat[i, 18] * ndata.iat[i, 19] * (1 - (ndata.iat[-1,14].date() - t).days / maxtime))
    result.append(sum(wdata)/len(wdata))
print(result)
num_encode = {
              'star_rating':{-1:1,-0.6:2,-0.2:3,0.6:4,1:5}
              }
data.replace(num_encode, inplace=True)
newdata=pd.DataFrame({"Wdata":wdata,"star_rating":list(data['star_rating'])})
# data["Wdata"]=wdata
newdata.to_csv("..//q3//423421857.csv",index=False)




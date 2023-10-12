import pandas as pd
from datetime import datetime
import time

data=pd.read_csv("./CE_venter_microwave.csv")
data['review_date'] = pd.to_datetime(data['review_date'], format="%m/%d/%Y")
data.sort_values("review_date",inplace=True)

print(data.iat[0,14])
print(data.iat[-1,14])


t0 =datetime.strptime('2009-12-31','%Y-%m-%d').date()
t1 =datetime.strptime('2012-12-31','%Y-%m-%d').date()
t2 =datetime.strptime('2015-12-31','%Y-%m-%d').date()
print(t0,t1,t2)

data_list=[]
data_list.append(data[data['review_date'].between(pd.to_datetime('2000-01-01'),pd.to_datetime('2009-12-31'))])
data_list.append(data[data['review_date'].between(pd.to_datetime('2000-01-01'),pd.to_datetime('2012-12-31'))])
data_list.append(data[data['review_date'].between(pd.to_datetime('2000-01-01'),pd.to_datetime('2015-12-31'))])
# data_list.append(data[data['review_date'].between(pd.to_datetime('2015-12-31'),pd.to_datetime('2015-08-31'))])
# print(data_list)

product=list(set(data['product_parent']))
result={}
for pro in product:
    ndata = data[data["product_parent"] == pro]
    ndata.index = [i for i in range(ndata.shape[0])]
    maxtime=(ndata.iat[-1,14].date()-ndata.iat[0,14].date()).days
    print(maxtime)
    wdata = [[], [], []]
    for i in range(ndata.shape[0]):
        t = ndata.iat[i, 14].date()
        if (t0 - t).days > 0:
            if ndata.iat[i, 18] < 0 and ndata.iat[i, 19] < 0:
                wdata[0].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t0 - t).days / (t0 - data.iat[0, 14].date()).days))
                wdata[1].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t1 - t).days / (t0 - data.iat[0, 14].date()).days))
                wdata[2].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t0 - data.iat[0, 14].date()).days))
            else:
                wdata[0].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t0 - t).days / (t0 - data.iat[0, 14].date()).days))
                wdata[1].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t1 - t).days / (t1 - data.iat[0, 14].date()).days))
                wdata[2].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t2 - data.iat[0, 14].date()).days))
        elif (t1 - t).days > 0:
            if ndata.iat[i, 18] < 0 and ndata.iat[i, 19] < 0:
                wdata[1].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t1 - t).days / (t1 - ndata.iat[0, 14].date()).days))
                wdata[2].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t2 - ndata.iat[0, 14].date()).days))
            else:
                wdata[1].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t1 - t).days / (t1 - ndata.iat[0, 14].date()).days))
                wdata[2].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t2 - ndata.iat[0, 14].date()).days))
        elif (t2 - t).days > 0:
            if ndata.iat[i, 18] < 0 and ndata.iat[i, 19] < 0:
                wdata[2].append(
                    -ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t2 - ndata.iat[0, 14].date()).days))
            else:
                wdata[2].append(
                    ndata.iat[i, 18] * ndata.iat[i, 19] * (1-(t2 - t).days / (t2 - ndata.iat[0, 14].date()).days))
        else:
            pass
        # print(wdata)
    hdata = []
    for w in wdata:
        if sum(w) == 0:
            hdata.append(0)
        else:
            hdata.append(sum(w) / len(w))

    result[str(pro)] = hdata

print(result)

result=pd.DataFrame(result)
result.to_csv("T_microwave.csv",index=False)

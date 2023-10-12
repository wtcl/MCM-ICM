import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

data=pd.read_csv("../data/pacifier.csv")
# hair_dryer  732252283
# microwave   423421857
# pacifier    246038397

data=data[data['product_parent']==246038397]
data['review_date'] = pd.to_datetime(data['review_date'], format="%m/%d/%Y")
data.sort_values("review_date",inplace=True)
data.resample('Q',on='review_date')
data.index=[i for i in range(data.shape[0])]
x1=[]
x2=[]
y1=[]
y2=[]

for i in range(data.shape[0]):
    t=str(data.iat[i,14])
    today = pd.to_datetime(t) - datetime.timedelta(93)
    quarter_start_day = datetime.date(today.year, today.month - (today.month - 1) % 3, 1).isoformat()
    quarter_end_day = (datetime.date(today.year, today.month - (today.month - 1) % 3 + 2, 1) + relativedelta(months=1,
                                                                                                             days=-1)).isoformat()
    data_new = (data[data['review_date'].between(quarter_start_day, quarter_end_day)])
    data_x1 = data_new[data_new['star_rating'] == 4].shape[0] + data_new[data_new['star_rating'] == 5].shape[0]
    data_y1 = data_new[data_new['star_rating'] == 1].shape[0] + data_new[data_new['star_rating'] == 2].shape[0]

    today = pd.to_datetime(t) + datetime.timedelta(93)
    quarter_start_day = datetime.date(today.year, today.month - (today.month - 1) % 3, 1).isoformat()
    quarter_end_day = (datetime.date(today.year, today.month - (today.month - 1) % 3 + 2, 1) + relativedelta(months=1,
                                                                                                             days=-1)).isoformat()
    data_new = (data[data['review_date'].between(quarter_start_day, quarter_end_day)])
    data_x2 = data_new[data_new['star_rating'] == 4].shape[0] + data_new[data_new['star_rating'] == 5].shape[0]
    data_y2 = data_new[data_new['star_rating'] == 1].shape[0] + data_new[data_new['star_rating'] == 2].shape[0]
    print(data_x1,data_x2,data_y1,data_y2)
    x1.append(data_x1)
    x2.append(data_x2)
    y1.append(data_y1)
    y2.append(data_y2)
xy=pd.DataFrame({"x1":x1,"y1":y1,"x2":x2,"y2":y2})
xy.to_csv("xy_data_246038397.csv",index=False)
import pandas as pd

data=pd.read_csv("./CE_venter_hair_dryer.csv")
data['review_date'] = pd.to_datetime(data['review_date'], format="%m/%d/%Y")
data.sort_values("review_date",inplace=True)

data=data[data['product_parent']==47684938]
del data['product_parent']

print(data)
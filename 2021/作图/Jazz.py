import pandas as pd
import csv

# data=pd.read_csv("../data/influence_data.csv")
# typeid={}
# for i in range(data.shape[0]):
#     typeid['['+str(data.iat[i,0])+']']=data.iat[i,2]
#     typeid['['+str(data.iat[i,4])+']']=data.iat[i,6]

# with open('./full.txt',encoding='utf-8') as f:
#     lines=f.readlines()
#     for line in lines:
#         if len(line.split(','))==19:
#             with open("newfull.csv", 'a', encoding='utf-8') as ff:
#                 ff.write(line)

# data_full=pd.read_csv("./newfull.csv")
# print(data_full)
# print(typeid)
# type=[]
# for i in range(data_full.shape[0]):
#     try:
#         type.append(typeid[data_full.iat[i,1]])
#     except:
#         type.append("xxx")
# data_full['type']=type
# data_full=data_full[data_full['type']=='Jazz']
# data_full.to_csv("Jazz_data.csv",index=False)

data=pd.read_csv("Jazz_data.csv")
del data['artists_id']
del data['artist_names']
del data['type']
del data['song_title (censored)']
del data['release_date']
yeardata=[]
for i in range(1924,2020):
    datai=data[data['year']==i]
    ti=[]
    if datai.empty!=True:
        for col in list(datai.columns):
            ti.append(sum(datai[col])/len(datai[col]))
    print(ti)
    yeardata.append(ti)
print(yeardata)
f = open('jazzyeardata.csv','w',newline='')
writer = csv.writer(f)
for i in yeardata:
    if len(i)>0:
        writer.writerow(i)
f.close()

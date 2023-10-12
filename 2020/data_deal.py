import pandas as pd
import re

# data0=pd.read_csv("./data/hair_dryer.tsv",sep='\t')
# print(data0)
# print(data0[data0['review_body']==None])
# print(data0.columns.is_unique)


# data.to_csv("./data/hair_dryer.csv",index=False)
# data1=pd.read_csv("./data/microwave.tsv",sep='\t')
# print(len(list(data1['customer_id'])))
# print(len(set(list(data1['customer_id']))))
# for i in list(data1['customer_id']):
#     if list(data1['customer_id']).count(i)>1:
#         print(i)
# print(data1)
# for i in list(data1.T.index):
#     if len(list(data1[i]))==len(list(set(data1[i]))):
#         print(i) # 不重复

# data.to_csv("./data/microwave.csv",index=False)
# data2=pd.read_csv("./data/pacifier.tsv",sep='\t')
# data.to_csv("./data/pacifier.csv",index=False)
# print(data2)
# for i in list(data2.T.index):
#     if (data2[i].T.is_unique)==True:
#         print(i)

def get_sim(a,b):
    return (len(set(a)&set(b))/len(set(a+b)))


data0=pd.read_csv("./data//pacifier.csv")
review_list=[]

for i in range(data0.shape[0]):
    review_list.append(re.findall("[a-zA-Z]+",data0.iat[i,12]+' '+data0.iat[i,13]))

simi_num=[]
for i in range(len(review_list)):
    t=[]
    for j in range(len(review_list)):
        if len(review_list[i])>0 and len(review_list[j]) and get_sim(review_list[i],review_list[j])>=0.8 and i!=j:
            t.append(j)
            simi_num.append(i)
            break
print(simi_num)
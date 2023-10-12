import pandas as pd

data=pd.read_csv("../data/influence_data.csv")
# ['influencer_id', 'influencer_name', 'influencer_main_genre','influencer_active_start', 'follower_id', 'follower_name','follower_main_genre', 'follower_active_start']
# ['International', 'Country', 'New Age', 'Electronic', 'R&B;', 'Comedy/Spoken', 'Unknown', 'Stage & Screen', 'Vocal', 'Latin', 'Easy Listening', 'Religious', 'Jazz', 'Classical', 'Pop/Rock', 'Reggae', 'Blues', 'Folk', 'Avant-Garde', "Children's"]
front=list(data["influencer_main_genre"])
after=list(data["follower_main_genre"])
sample=(list(set(front)))
s={}  # 每种流派的跟随流派
for i in range(20):
    s[sample[i]]=[]
for i in range(data.shape[0]):
    s[front[i]].append(after[i])
snum={} # 跟随流派音乐家数量
for i in range(20):
    snum[sample[i]]=(len(s[sample[i]]))
    ss=s[sample[i]]
    s[sample[i]]=list(set(ss))
print(s)
print(sorted(snum.items(),key=lambda x:x[1],reverse=True))

t={}  # 每种流派的前置流派
for i in range(20):
    t[sample[i]]=[]
for i in range(data.shape[0]):
    t[after[i]].append(front[i])
tnum= {}  # 前置流派的数量
for i in range(20):
    tnum[sample[i]]=(len(t[sample[i]]))
    tt=t[sample[i]]
    t[sample[i]]=list(set(tt))
print(t)
print(sorted(tnum.items(),key=lambda x:x[1],reverse=True))

# side0=[]
# side1=[]
# for key ,vlaues in s.items():
#     for i in vlaues:
#         side0.append(key)
#         side1.append(i)
# newdata=pd.DataFrame({"id":[i for i in range(len(side0))],"source":side0,"target":side1})
# newdata.to_csv("side.csv",index=False)
#
# pointdata=pd.DataFrame({"id":sample,"label":sample})
# pointdata.to_csv("point.csv",index=False)

newdata=data[(data['influencer_main_genre']=='R&B;') | (data['follower_main_genre']=='R&B;')]
print(newdata)
newdata.to_csv("R&B.csv",index=False)
import pandas as pd

data=pd.read_csv("../data/full_music_data.csv")
bool=data["artist_names"].str.contains("', '")
newdata=data[bool==False]
# newdata=data[bool]
# newdata.to_excel("double.xlsx")
print(newdata.shape)
print(data.shape)

artist_data=pd.read_csv("../data/data_by_artist.csv")
print(artist_data.shape)
art0=list(set(artist_data['artist_id']))
print(len(art0))

artist_data1=pd.read_csv("../data/influence_data.csv")
art=[]
for i in range(artist_data1.shape[0]):
    art.append(artist_data1.iat[i,0])
    art.append(artist_data1.iat[i,4])
art=list(set(art))
print(len(art))

art2=list(set(art)-set(art0))
print(len(art2))

artist_id=list(set(art)-set(art2))
print(len(artist_id))

boollist=["["+str(i)+"]" for i in artist_id]
newdata=newdata[newdata["artists_id"].isin(boollist)]
print(len(list(set(newdata["artists_id"]))))

artist=list(set(newdata["artists_id"]))
print("artist:",len(artist))
print(artist)

newdata.to_csv("./our_data/full_data.csv",index=False)

artist_id=[int(i[1:-1]) for i in artist]

fluence_data=pd.read_csv("../data/influence_data.csv")
fluence_data=fluence_data[artist_data1["influencer_id"].isin(artist_id)]
fluence_data=fluence_data[fluence_data["follower_id"].isin(artist_id)]
fluence_data.to_csv("./our_data/influence_data.csv",index=False)
artist_data=pd.read_csv("../data/data_by_artist.csv")
artist_data=artist_data[artist_data['artist_id'].isin(artist_id)]
artist_data.to_csv("./our_data/data_by_artist.csv",index=False)

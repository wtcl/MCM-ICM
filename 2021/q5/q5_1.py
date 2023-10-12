# 针对年份处理
import pandas as pd
import numpy as np
import math

data_years=pd.read_csv("../data/data_by_year.csv")

max_min_scaler = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))
data_years['danceability']=data_years[['danceability']].apply(max_min_scaler)
data_years['energy']=data_years[['energy']].apply(max_min_scaler)
data_years['valence']=data_years[['valence']].apply(max_min_scaler)
data_years['tempo']=data_years[['tempo']].apply(max_min_scaler)
data_years['loudness']=data_years[['loudness']].apply(max_min_scaler)
# data_years['mode']=data_years[['mode']].apply(max_min_scaler)
data_years['key']=data_years[['key']].apply(max_min_scaler)
data_years['acousticness']=data_years[['acousticness']].apply(max_min_scaler)
data_years['instrumentalness']=data_years[['instrumentalness']].apply(max_min_scaler)
data_years['liveness']=data_years[['liveness']].apply(max_min_scaler)
data_years['speechiness']=data_years[['speechiness']].apply(max_min_scaler)
print(data_years)
data_years.to_csv("test.csv",index=False)

def cal_cos_star(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10):
    print(a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10)
    print(math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2))
    print(math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2))
    print('-----')
    return ((a1*b1+a2*b2+a3*b3+a4*b4+a5*b5+a6*b6+a7*b7+a8*b8+a9*b9+a10*b10)/
            (math.sqrt(a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2)*
             math.sqrt(b1**2+b2**2+b3**2+b4**2+b5**2+b6**2+b7**2+b8**2+b9**2+b10**2)))
similarity=[]
for i in range(data_years.shape[0]-1):
    similarity.append(
        cal_cos_star(
            data_years.iat[i,1],data_years.iat[i,2],data_years.iat[i,3],data_years.iat[i,4],
            data_years.iat[i,5],data_years.iat[i,7],data_years.iat[i,8],
            data_years.iat[i,9],data_years.iat[i,10],data_years.iat[i,11],
            data_years.iat[i+1, 1], data_years.iat[i+1, 2], data_years.iat[i+1, 3], data_years.iat[i+1, 4],
            data_years.iat[i+1, 5], data_years.iat[i+1, 7], data_years.iat[i+1, 8],
            data_years.iat[i+1, 9], data_years.iat[i+1, 10], data_years.iat[i+1, 11]
        )
    )
print(similarity)
years_similarity=pd.DataFrame({"year":list(data_years['year'])[:-1],"similarity":similarity})
years_similarity.to_csv("years_similarity.csv",index=False)
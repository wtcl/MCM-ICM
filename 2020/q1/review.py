import pandas as pd

def cal_num(data):
    frame_list = []
    star_num = []

    for i in range(1, 6):
        frame_list.append(data[data["star_rating"] == i])
    for frame in frame_list:
        star_num.append(frame.shape[0])

    return star_num

data0=pd.read_csv("../data//hair_dryer.csv")
data1=pd.read_csv("../data//microwave.csv")
data2=pd.read_csv("../data//pacifier.csv")

s0=cal_num(data0)
s1=cal_num(data1)
s2=cal_num(data2)

num_data=pd.DataFrame({"hair_dryer":s0,"microwave":s1,"pacifier":s2})
num_data.to_csv("star.csv",index=False)

import pandas as pd

def data_deal(name,data):
    with open("D://desktop//数据摘要.txt", 'a', encoding='utf-8') as f:
        f.write(name+" : \n\n")
    n = 0
    index_list = list(data.T.index)
    for index_name in index_list:
        line_con = str(n) + '. ' + str(index_name) + ' : '
        n += 1
        before_list = list(data[index_name])
        after_list = list(set(data[index_name]))
        if data[index_name].dtype == 'int64':
            line_con += '整数'
            line_con = line_con + ', 最大值为：' + str(max(before_list))
            line_con = line_con + ', 最小值为：' + str(min(before_list))
        elif data[index_name].dtype == 'float64':
            line_con += '小数'
            line_con = line_con + ', 最大值为：' + str(max(before_list))
            line_con = line_con + ', 最小值为：' + str(min(before_list))
        else:
            line_con += '字符串'
        if len(before_list) == len(after_list):
            line_con += ', 无重复值'
        else:
            line_con += ', 有重复值'
            if len(after_list) < 25:
                line_con += '，所有数据均为' + ', '.join(str(e) for e in after_list)
        print(line_con)
        with open("D://desktop//数据摘要.txt", 'a', encoding='utf-8') as f:
            f.write(line_con + '\n')
    with open("D://desktop//数据摘要.txt", 'a', encoding='utf-8') as f:
        f.write('一共{}条数据'.format(str(data.shape[0])))
        f.write('\n\n\n')

data=pd.read_csv("../2020/data//hair_dryer.csv")
data1=pd.read_csv("../2020/data//microwave.csv")
data2=pd.read_csv("../2020/data//pacifier.csv")
data_deal('hair_dryer',data)
data_deal('microwave',data1)
data_deal('pacifier',data2)


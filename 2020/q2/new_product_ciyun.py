import pandas
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba

# hair_dryer  落榜者：238410319 蝉联：47684938  新晋：732252283
# microwave   蝉联：295520151 落榜者：109226352 新晋：523301568
# pacifier    蝉联：246038397  落榜：604039789  新晋: 667171015

# 数据获取
text=''
data=pd.read_csv("../data//pacifier.csv")
data=data[data['product_parent']==246038397]
for i in range(data.shape[0]):
    text+=data.iat[i,12]+' '+data.iat[i,13]

mask=np.array(Image.open("../q1//pacifier.jpeg"))

# 数据清洗
# 屏蔽45
STOPWORDS=["and","it","the","this","I","of","to","is","was","in","on","at","for","that","my","a","an",
           "hair","dryer","one","with","have","t","had","br","you","but"]

# font=r'C:\Windows\Fonts\simhei.ttf'
sep_list=jieba.lcut_for_search(text,)
# sep_list=[]
# for i in sep:
#     if i.flag in ["eng"]:
#         sep_list.append(list(i)[0])
# print(sep_list)
sep_list=" ".join(sep_list)

wc=WordCloud(
    scale=4,#调整图片大小---（如果设置太小图会很模糊）
    # font_path=font,#使用的字体库
    max_words=200,  # 词云显示的最大词数
    margin=2,#字体之间的间距
    mask=mask,#背景图片
    background_color='white', #背景颜色
    max_font_size=200,
    # min_font_size=1,
    stopwords=STOPWORDS, #屏蔽的内容
    collocations=False, #避免重复单词
    width=1600,height=1200 #图像宽高，字间距
)

wc.generate(sep_list) #制作词云
wc.to_file('246038397.jpg') #保存到当地文件
print(wc.words_)
# 图片展示
plt.figure(dpi=100) #通过这里可以放大或缩小
plt.imshow(wc,interpolation='catrom')
plt.axis('off')
plt.show()
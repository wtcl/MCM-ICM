import pandas as pd
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba

data=pd.read_csv("../data//pacifier.csv")
data=data[data['star_rating']>3]
STOPWORDS=["and","it","the","this","I","of","to","is","was","in","on","at","for","that","my","a","an",
           "hair","dryer","one","with","have","t","had","br","you"]
text=''
for i in range(data.shape[0]):
    text+=data.iat[i,12]+' '+data.iat[i,13]+' '
sep_list=jieba.lcut_for_search(text,)
sep_list=" ".join(sep_list)
wc=WordCloud(
    scale=4,#调整图片大小---（如果设置太小图会很模糊）
    # font_path=font,#使用的字体库
    max_words=200000000,  # 词云显示的最大词数
    margin=2,#字体之间的间距
    # mask=mask,#背景图片
    background_color='white', #背景颜色
    max_font_size=200,
    # min_font_size=1,
    stopwords=STOPWORDS, #屏蔽的内容
    collocations=False, #避免重复单词
    width=1600,height=1200 #图像宽高，字间距
)
wc.generate(sep_list)
words=wc.words_
print(words)
new=pd.DataFrame({"keys":words.keys(),"values":words.values()})
new.to_csv("emotion_star_pacifier_45.csv",index=False)

"""
tb=Blobber(analyzer=NaiveBayesAnalyzer())
data=pd.read_csv("../data//microwave.csv")
data=data[data["star_rating"]<3]
emotion=[]
for i in range(data.shape[0]):
    emotion.append(tb(data.iat[i,12]+' '+data.iat[i,13]).sentiment.p_pos)
print(emotion)

newdata=pd.DataFrame({"star":list(data['star_rating']),"emotion":emotion})
print(newdata.corr(method='spearman'))
"""


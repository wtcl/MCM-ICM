from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba
import pandas as pd
from textblob import TextBlob

def wc(text,pic):

    # mask = np.array(Image.open("hair_dryer.jpeg"))
    mask=np.array(Image.open(pic))

    STOPWORDS = ["and", "it", "the", "this", "I", "of", "to", "is", "was", "in", "on", "at", "for", "that", "my", "a",
                 "an", "one", "with", "have", "t", "had", "br", "you","but","they","as"]

    sep_list = jieba.lcut_for_search(text, )
    sep_list = " ".join(sep_list)
    wc = WordCloud(
        scale=4,  # 调整图片大小---（如果设置太小图会很模糊）
        max_words=1000,  # 词云显示的最大词数
        margin=2,  # 字体之间的间距
        mask=mask,  # 背景图片
        background_color='white',  # 背景颜色
        max_font_size=250,
        # min_font_size=1,
        stopwords=STOPWORDS,  # 屏蔽的内容
        collocations=False,  # 避免重复单词
        width=1600, height=1200  # 图像宽高，字间距
    )

    wc.generate(sep_list)  # 制作词云
    wc.to_file(pic[:-4]+"png")  # 保存到当地文件

    # 图片展示
    plt.figure(dpi=100)  # 通过这里可以放大或缩小
    plt.imshow(wc, interpolation='catrom')
    plt.axis('off')
    plt.show()

    # 词频
    words=wc.words_
    return words

data0=pd.read_csv("../data//hair_dryer.csv")
data1=pd.read_csv("../data//microwave.csv")
data2=pd.read_csv("../data//pacifier.csv")

c0=''
c1=''
c2=''

for i in range(data0.shape[0]):
    c0=c0+data0.iat[i,12]+' '+data0.iat[i,13]+' '
for i in range(data1.shape[0]):
    c1=c1+data1.iat[i,12]+' '+data1.iat[i,13]+' '
for i in range(data2.shape[0]):
    c2=c2+data2.iat[i,12]+' '+data2.iat[i,13]+' '


word0=wc(c0,"hair_dryer.jpeg")
word1=wc(c1,"microwave.jpeg")
word2=wc(c2,"pacifier.jpeg")

w0=pd.DataFrame([word0]).T
w1=pd.DataFrame([word1]).T
w2=pd.DataFrame([word2]).T

w0.to_csv("hair_dryer_words.csv")
w1.to_csv("microwave_words.csv")
w2.to_csv("pacifier_words.csv")

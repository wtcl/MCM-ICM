from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba


# 数据获取
with open("5.txt",'r', encoding='utf-8')as f:
    text=f.read()

mask=np.array(Image.open("hair_dryer.jpeg"))

# 数据清洗
# 屏蔽45
STOPWORDS=["and","it","the","this","I","of","to","is","was","in","on","at","for","that","my","a","an",
           "hair","dryer","one","with","have","t","had","br","you"]

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
wc.to_file('5.jpg') #保存到当地文件
print(wc.words_)
# 图片展示
plt.figure(dpi=100) #通过这里可以放大或缩小
plt.imshow(wc,interpolation='catrom')
plt.axis('off')
plt.show()
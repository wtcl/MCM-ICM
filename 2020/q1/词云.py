# coding:utf-8
import jieba
import wordcloud

with open("1.txt", "r", encoding="utf-8") as f:
    t=f.readlines()
    for line in t:
        ls = jieba.lcut(line)
        print(list(set(ls)))
txt = "".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("growordcloud.png")
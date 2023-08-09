# 选做题就这样吧，实在搞不清人物别称
from xml.etree.ElementInclude import include
import jieba
excludes = {"什么","一个","我们","你们","如今","说道","知道","起来","这里","出来","众人","那里","自己","一面","只见","两个","没有","怎么","不是","布置","这个","这个","听见","这样","进来"}
txt = open("202111040246\红楼梦.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "宝玉" or word == "宝二爷":
        rword = "贾宝玉"
    elif word == "王夫人" or word == "凤姐":
        rword = "王熙凤"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))
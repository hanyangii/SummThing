# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsKorean
from TF_IDF import * 

url  = 'http://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=001&aid=0008930270&isYeonhapFlash=Y&rc=N'
url1 = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0008929838'
url2 = 'http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0008929542&date=20170102&type=1&rankingSeq=1&rankingSectionId=102'
g = Goose({'stopwords_class':StopWordsKorean})

article = g.extract(url=url)
article1 = g.extract(url=url1)
article2 = g.extract(url=url2)

doc = [article.cleaned_text, article1.cleaned_text, article2.cleaned_text]

#print article.title

#print '--------------'
#print article.cleaned_text
TF_IDF_url(doc)




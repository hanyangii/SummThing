# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsKorean
from TF_IDF import *
from SentenceExtraction import *

url  = 'http://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=001&aid=0008930270&isYeonhapFlash=Y&rc=N'
url1 = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0008929838'
url2 = 'http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0008929542&date=20170102&type=1&rankingSeq=1&rankingSectionId=102'
g = Goose({'stopwords_class':StopWordsKorean})

article = g.extract(url=url)
article1 = g.extract(url=url1)
article2 = g.extract(url=url2)

doc = [article.cleaned_text.split('=')[2], article1.cleaned_text.split('=')[2], article2.cleaned_text.split('=')[2]]

#print article.title

#print '--------------'
#print article.cleaned_text

#topic_words=TF_IDF_url(doc)

wordd=["지지율","총장","개헌","여론조사","반응","정씨","특검","수배","변호인","귀국","고양이","길고양이","사람","감염","우려"]

scores=[0.00651,0.00597,0.00489,0.0038,0.00326,0.01892,0.00946,0.00676,0.00541,0.00541,0.0202,0.01926,0.00846,0.00752,0.00658]

topic_words=[]
for k in range(3):
	tt=[]
	for t in range(5):
		tt.append([wordd[k*5+t],scores[k*5+t]])
	topic_words.append(tt)

print topic_words
for i in range(len(topic_words)):
	sentences=SplitTextfile(doc[i])
#	sentences=sentences[1:]

	score=[0 for l in range(len(sentences))]
	topic_word=topic_words[i]
	for word in topic_word:
		for j in range(len(sentences)):
			score[j]=score[j]+sentences[j].count(word[0])*word[1]
	
	for t in range(len(sentences)):
		sentences[t]=[sentences[t],score[t],t]

	sorted_sentences = sorted(sentences, key=lambda l:l[1], reverse=True)
	
	for j in sorted_sentences[0:5]:
		print j[2], j[0], j[1]
		print '\n'
	print '\n\n'
	

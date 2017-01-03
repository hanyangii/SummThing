# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsKorean

import numpy as np
import sys
import math

from TF_IDF import *
from SentenceExtraction import *

reload(sys)
sys.setdefaultencoding('utf-8')

#Extract an article from url
url = open('data/url.txt','r').read()
g = Goose({'stopwords_class':StopWordsKorean})

article = g.extract(url=url).cleaned_text

#Calcurate TF-IDF
all_dic = np.load('data/NounsCount.npy').tolist()
nouns = noun_list(article)
tfidf = []
for noun in nouns:
	if noun in all_dic:
		n_contains = all_dic[noun]
		idf_score = math.log(len(n_contains)+1)/(2+sum(1 for i in n_contains if i>0))
	else:
		a = list(all_dic.keys())
		idf_score = math.log(len(all_dic[a[1]])+1)/2
	tf_score = tf(noun, article)
	pair = [noun,tf_score*idf_score]
	tfidf.append(pair)

tfidf = sorted(tfidf, key=lambda l:l[1], reverse=True)
topic_words=tfidf[:5]


#Extract Sentences
sentences = SplitTextfile(article)
score= [0 for i in range(len(sentences))]

for word in topic_words:
	print word[0]
	for j in range(len(sentences)):
		score[j]=score[j]+sentences[j].count(word[0])*word[1]

for j in range(len(sentences)):		
	sentences[j]=[sentences[j],score[j],j]

sorted_sentences = sorted(sentences, key=lambda l:l[1], reverse=True)
topic_sentences = sorted_sentences[:5]
topic_sentences = sorted(topic_sentences, key=lambda l:l[2])

for j in topic_sentences[0:5]:
	print j[2], j[0], j[1]
	print '\n'
print '\n\n'
	

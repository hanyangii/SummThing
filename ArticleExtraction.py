# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsKorean
#from konlpy.tag import Mecab
from nltk import collocations
from konlpy.utils import pprint

import numpy as np
import sys
import math

from Collocation import *
from TF_IDF import *
from SentenceExtraction import *
import os
os.environ['PYTHON_EGG_CACHE'] = '/Users/jeongjiwon'
#os.environ['PYTHON_EGG_CACHE'] = '/tmp'
reload(sys)
sys.setdefaultencoding('utf-8')

#Extract article from url
def article_from_url(url):
	g = Goose({'stopwords_class':StopWordsKorean})
	return g.extract(url=url)


url = open('./data/url.txt','r').read()
article = article_from_url(url)
article = article.cleaned_text

#merge collocation words
nouns = get_nouns(article)
word_pairs = get_collocation_pairs(article, './data/PosData.npy')

#Calcurate TF-IDF
all_dic = np.load('./data/NounsCount.npy').tolist()
tfidf = []
for noun in nouns:
	idf_score = trained_idf(noun,all_dic)

	tf_score = tf(noun, article)
	new_pair = [noun,tf_score*idf_score,idf_score]
	tfidf.append(new_pair)

tfidf = sorted(tfidf, key=lambda l:l[1], reverse=True)
topic_words=tfidf[:5]
pprint(topic_words)
save_words=list(topic_words)

for i in range(len(save_words)):
	for j in range(i,len(save_words)):
		p1=[save_words[i][0],save_words[j][0]]
		p2=[save_words[j][0],save_words[i][0]]
		contain = False
		if p1 in word_pairs :
			add_pair=p1
			contain=True
		elif p2 in word_pairs:
			add_pair=p2
			contain=True
		
		#Append collocation words and re-calcurate TF-IDF
		if contain==True:
			#Calcurate new TF-IDF
			collocation = [[add_pair[0]+add_pair[1]],[add_pair[0]+' '+add_pair[1]]]
			
			for col in collocation:
				idf_score = trained_idf(col[0],all_dic)

				gnd = get_nouns_duplicate(article)
				n_tf = float(article.count(col[0]))/float(len(gnd))
				col.append(n_tf*idf_score)
				col.append(idf_score)
			
			tmp = save_words[i][1]/save_words[i][2]-collocation[0][1]-collocation[1][1]
			collocation.append([save_words[i][0],tmp,save_words[i][2]])
			tmp = save_words[j][1]/save_words[j][2]-collocation[0][1]-collocation[1][1]
			collocation.append([save_words[j][0],tmp,save_words[j][2]])
			topic_words.remove(save_words[i])
			topic_words.remove(save_words[j])
			
			for col in collocation :
				topic_words.append(col)

#Extract Sentences
sentences = SplitTextfile(article)
score= [0 for i in range(len(sentences))]

WordFile = open('./data/writeWord.txt','w')

for word in topic_words:
	WordFile.write(word[0]+'\n')
	for j in range(len(sentences)):
		score[j]=score[j]+sentences[j].count(word[0])*word[1]

for j in range(len(sentences)):		
	sentences[j]=[sentences[j],score[j],j]

sorted_sentences = sorted(sentences, key=lambda l:l[1], reverse=True)
topic_sentences = sorted_sentences[:5]
topic_sentences = sorted(topic_sentences, key=lambda l:l[2])

SentenceFile = open('./data/writeTest.txt','w')

for j in topic_sentences[0:5]:
	SentenceFile.write(j[0]+'\n')

SentenceFile.close()
WordFile.close()

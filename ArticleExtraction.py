# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsKorean
from konlpy.tag import Kkma
from nltk import collocations
from konlpy.utils import pprint

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

#merge collocation words
nouns = get_nouns(article)
measures = collocations.BigramAssocMeasures()
tagged_words = Kkma().pos(article)
finder = collocations.BigramCollocationFinder.from_words(tagged_words)
score_words = finder.score_ngrams(measures.likelihood_ratio)

find_words = ['NNG','NNB','NNP']
collocs=[]
word_pairs=[]
for pair in score_words:
	if pair[0][0][1] in find_words and pair[0][1][1] in find_words:
		if pair[1] > 25.0 : 
			collocs.append(pair)
			pp = [pair[0][0][0],pair[0][1][0]]
			word_pairs.append(pp)

#Calcurate TF-IDF
all_dic = np.load('data/NounsCount.npy').tolist()
tfidf = []
for noun in nouns:
	if noun in all_dic:
		n_contains = all_dic[noun]
		idf_score = math.log(len(n_contains)+1)/(2+sum(1 for i in n_contains if i>0))
	else:
		a = list(all_dic.keys())
		idf_score = math.log(len(all_dic[a[1]])+1)/2
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
				if col[0] in all_dic:
					n_contains = all_dic[col[0]]
					idf_score = math.log(len(n_contains)+1)/(2+sum(1 for i in n_contains if i>0))
				else:
					a = list(all_dic.keys())
					idf_score = math.log(len(all_dic[a[1]])+1)/2
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

pprint(topic_words)

for word in topic_words:
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
	

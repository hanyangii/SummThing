#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
from konlpy.utils import pprint
from goose import Goose
from goose.text import StopWordsKorean

import json
import math
import sys
import newspaper
import numpy as np

from Collocation import *
from ExtractNouns import *

reload(sys)
sys.setdefaultencoding('utf-8')

#load train articles
TrainFile=open('data/train_articles.txt','r')
articles=[]
g = Goose({'stopwords_class':StopWordsKorean})
while True:
	line = TrainFile.readline()
	line= line.split('\n')[0]
	if not line : break
	new_article=newspaper.Article(line)
	new_article.download()
	new_article.parse()
	articles.append(new_article.text)

#Save number of nouns --> dictionary = {"noun":[article1_cnt, article2_cnt, ....]}
all_dict={}
for i, article in enumerate(articles):
	nouns = get_nouns(article)

	#Add collocation words
	word_pairs = get_collocation_pairs(article,False)

	save_words={}
	for pair in word_pairs:
		save_words[pair[0]]=pair[1]
		save_words[pair[1]]=pair[0]
		nouns.append(pair[0]+pair[1])
		nouns.append(pair[0]+' '+pair[1])

	for noun in nouns:
		if noun not in all_dict:
			all_dict[noun]=[0 for j in range(len(articles))]
		
		cnt=[0 for index in range(4)]
		if noun in list(save_words.keys()):
			cnt[1] = article.count(noun+save_words[noun])
			cnt[2] = article.count(noun+' '+save_words[noun])
			cnt[3] = article.count(save_words[noun]+noun)
			cnt[0]= article.count(save_words[noun]+' '+noun)

		all_dict[noun][i]=all_dict[noun][i]+article.count(noun)-sum(cnt)
np.save('data/NounsCount.npy', all_dict)

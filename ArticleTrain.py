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

from ExtractNouns import *

reload(sys)
sys.setdefaultencoding('utf-8')

#load train articles
TrainFile=open('data/train_articles.txt','r')
articles=[]
g = Goose({'stopwords_class':StopWordsKorean})
while True:
	line = TrainFile.readline()
	if not line : break
	new_article=newspaper.Article(line)
	new_article.download()
	new_article.parse()
	articles.append(new_article.text)

#Save number of nouns --> dictionary = {"noun":[article1_cnt, article2_cnt, ....]}
all_dict={}
#fi=open('temp.txt','w')
for i, article in enumerate(articles):
	nouns = noun_list(article)
	#fi.write(article)
	for noun in nouns:
		if noun not in all_dict:
			all_dict[noun]=[0 for j in range(len(articles))]
		all_dict[noun][i]=all_dict[noun][i]+article.count(noun)

np.save('data/NounsCount.npy', all_dict)

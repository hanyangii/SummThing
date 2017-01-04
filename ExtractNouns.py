#!/usr/bin/env python
# -*- coding: utf-8 -*-

from konlpy.tag import Mecab
from konlpy.utils import pprint
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#read from local file
def read_text(fileName):
	location = '../SummThing/data/%s.txt' %fileName
	print fileName
	with open(location, 'r') as f:
		doc = f.read().decode('utf-8')
	f.close()
	return doc

def get_nouns_duplicate(text):
	mecab = Mecab()
	arr = mecab.nouns(text)
	return arr

def get_nouns(text, chunk=500, mfv=20):
	mecab = Mecab()
	arr = mecab.nouns(text)
	return list(set(arr))

#	for i in range(len(arr)/chunk):
#		nngs = []
#		for j in range(chunk):
			
#			if arr[i*chunk + j][1] in ['NNG', 'NNP']:
#				nngs.append(arr[i*chunk + j][0])
	
#		count = Counter(nngs)
#		brr = count.most_common(mfv)
#		pprint(brr)
#	return brr	

if __name__ == "__main__":
	data_name = '소나기'
	text = read_text(data_name)
	nouns = get_nouns(text)
	pprint(nouns)

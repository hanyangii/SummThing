#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
import math
#from textblob import TextBlob as tb

#from konlpy.tag import Kkma
#from konlpy.utils import pprint
from ExtractNouns import get_nouns
from ExtractNouns import read_text


def tf(word, blob):
#	return blob.words.count(word) / len(blob.words)
#	print((get_nouns(blob)).count(word), len(get_nouns(blob)))
	return (get_nouns(blob)).count(word) / len(get_nouns(blob))

def n_containing(word, bloblist):
#	return sum(1 for blob in bloblist if word in blob.words)
	return sum(1 for blob in bloblist if word in get_nouns(blob))

def idf(word, bloblist):
	return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)


document_name1 = '말안듣는청개구리s'
document_name2 = '선녀와나무꾼s'
document_name3 = '해와달이된오누이s'

document1 = read_text(document_name1)
document2 = read_text(document_name2)
document3 = read_text(document_name3)

bloblist = [document1, document2, document3]


for i, blob in enumerate(bloblist):
#pprint(get_nouns(blob))
	print("Top words in document {}".format(i + 1))
	scores = {word: tfidf(word, blob, bloblist) for word in get_nouns(blob)}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	for word, score in sorted_words[:10]:
		print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))



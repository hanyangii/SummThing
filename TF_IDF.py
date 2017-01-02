#!/usr/bin/env python
# -*- coding: utf-8 -*-


#This Class extracts major Nouns using TF-IDF Algorithm 



from __future__ import division, unicode_literals
import math
from ExtractNouns import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#class to save text document information
class Textdoc:
	def __init__(self):
		self.title=''
		self.topic_words=[]
		self.content=''
	
	def save_title(self,title):
		self.title=title
	
	def add_word(self,word,score):
		word_pair=[word,score]
		self.topic_words.append(word_pair)
	
	def save_content(self,content):
		self.content=content


def tf(word, blob):
	return (get_nouns(blob)).count(word) / len(get_nouns(blob))

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in get_nouns(blob))

def idf(word, bloblist):
	return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)

def TF_IDF():
	doc_list=[]
	#The name of book is written on tran_data.txt
	TrainFile=open('data/train_data.txt')
	bloblist=[]
	while True:
		train_title = TrainFile.readline().split('\n')[0]
		if not train_title: break
		print train_title
		doc_class = Textdoc()
		doc_class.save_title(train_title)
		doc_class.save_content(read_text(train_title))
		doc_list.append(doc_class)
		bloblist.append(doc_class.content)

	"""
	document_name1 = '말안듣는청개구리s'
	document_name2 = '선녀와나무꾼s'
	document_name3 = '해와달이된오누이s'

	document1 = read_text(document_name1)
	document2 = read_text(document_name2)
	document3 = read_text(document_name3)

	bloblist = [document1, document2, document3]
	"""
	t=0
	for i, blob in enumerate(bloblist):
	#pprint(get_nouns(blob))
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist) for word in get_nouns(blob)}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:5]:
			doc_list[t].add_word(word, round(score, 5))
			#print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
		t=t+1
	
	return doc_list

def TF_IDF_url(doc_list):
	#doc_list=[]
	#The name of book is written on tran_data.txt
	#TrainFile=open('data/train_data.txt')
	#doc1 = doc_list[0]
	#doc2 = doc_list[1]
	#doc3 = doc_list[2]
	
	#bloblist=[doc1, doc2, doc3]
	for i, blob in enumerate(doc_list):
		#pprint(get_nouns(blob))
		nouns=get_nouns(blob)
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, doc_list) for word in nouns}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:5]:
			#doc_list[t].add_word(word, round(score, 5))
			print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
	
	#return doc_list
#if __name__=='__main__':


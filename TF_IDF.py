#!/usr/bin/env python
# -*- coding: utf-8 -*-


#This Class extracts major Nouns using TF-IDF Algorithm 


from __future__ import division, unicode_literals
import math
from ExtractNouns import *
import sys
from goose import Goose
from goose.text import StopWordsKorean

reload(sys)
sys.setdefaultencoding('utf-8')

#class to save text document information
class Textdoc:
	def __init__(self):
		self.title=''
		self.topic_words=[]
		self.content=''
		self.date=''
		self.url=''

	def save_article(self, title, url, date):
		self.title=title
		self.date=date
		self.url=url
	
	def save_title(self,title):
		self.title=title
	
	def add_word(self,word,score):
		word_pair=[word,score]
		self.topic_words.append(word_pair)
	
	def save_content(self,content):
		self.content=content
	
	def pop_article(self):
		return self.title, self.date, self.url


def tf(word, blob):
	gnd = get_nouns_duplicate(blob)
	return gnd.count(word) / len(gnd)

def trained_idf(word,all_dic):
	if word in all_dic:
		n_contains = all_dic[word]
		idf_score = math.log(len(n_contains) + 1) / (2 + sum(1 for i in n_contains if i > 0))
	else:
		a = list(all_dic.keys())
		idf_score = math.log(len(all_dic[a[1]]) + 1) / 2
	return idf_score

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
		#print train_title
		doc_class = Textdoc()
		doc_class.save_title(train_title)
		doc_class.save_content(read_text(train_title))
		doc_list.append(doc_class)
		bloblist.append(doc_class.content)

	t=0
	for i, blob in enumerate(bloblist):
	#pprint(get_nouns(blob))
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist) for word in get_nouns(blob)}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:5]:
			doc_list[t].add_word(word, round(score, 5))
#			print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
		t=t+1

	return doc_list

def TF_IDF_url():
	doc_list= []
	bloblist = []
	#The name of book is written on tran_data.txt
	f = open('data/train_data1.txt')
	g = Goose({'stopwords_class':StopWordsKorean})
	
	lines = f.readlines()
	f.close()

	for line in lines:
		doc_class = Textdoc()
		doc_class.save_title(g.extract(url=line).title)
		doc_class.save_content(g.extract(url=line).cleaned_text)
		doc_list.append(doc_class)
		bloblist.append(doc_class.content)	
#		print doc_class.content
	
	t=0
	for i, blob in enumerate(bloblist):
		#pprint(get_nouns(blob))
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist ) for word in get_nouns(blob)}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:5]:
			doc_list[t].add_word(word, round(score, 5))
#			print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
		t=t+1
	
	return doc_list



if __name__ == "__main__":
	TF_IDF_url()

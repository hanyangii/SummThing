#-*- coding: utf-8 -*-

#Split text file to sentences 
#Extract sentences including topic words.

from konlpy.tag import Kkma
from konlpy.utils import pprint

import nltk.data
import sys
import re


reload(sys)
sys.setdefaultencoding('utf-8')

#Split text file to sentences
def SplitTextfile(content):
	

	content = remove_interviewer(content)
	content = content.replace('\n', '')
	content = content.replace('다.','다.^^^' )
	output = content.split('^^^')

	return output



def SentenceExtract(file_name, content,topic_words):
	
	#Split text file to sentences 
	sentences=SplitTextfile(content)
	
	#Make words - sentences matrix
	score=[0 for i in range(len(sentences))]
	for word in topic_words:
		for i in range(len(sentences)):
			score[i]=score[i]+sentences[i].count(word[0])

		
	#Attatch (sentence, score) and Sorting 
	for i in range(len(sentences)):
		sentences[i]=[sentences[i],score[i],i]
	
	sorted_sentences = sorted(sentences, key=lambda l:l[1], reverse=True)
	topic_sentences = sorted_sentences[0:int(len(sorted_sentences)*0.5)]
	topic_sentences = sorted(topic_sentences, key=lambda l:l[2])

	for i in topic_sentences:
		print i[2], i[0], i[1]

	print '\n'

def Extraction(topic_words):
	for i in topic_words:
		SentenceExtract(i.title, i.content, i.topic_words)

def remove_interviewer(sentence):

	sentence_matched1 = re.findall(r".*[\=].*[\=]",sentence)
#	print sentence_matched1
	if sentence_matched1 != None:
#		print "1"
		#(서울=연합뉴스) 김아람 기자= 제거
		sentence = re.sub(r".*[\=].*[\=]", r"", sentence)
	
	sentence_matched2 = re.findall(r"[\[].*[\]]",sentence)
	if sentence_matched2 != None :
#		print "2"
		#[스포츠 조선 최보란 기자] 제거
		sentence = re.sub(r"[\[].*[\]]", r"",sentence)

	return sentence

if __name__ == "__main__":
	remove_interviewer('(Seoul=news) interview= remove')
	

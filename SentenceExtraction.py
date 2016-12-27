#-*- coding: utf-8 -*-

#Split text file to sentences 
#Extract sentences including topic words.

import sys
from konlpy.tag import Kkma
from konlpy.utils import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

#Split text file to sentences
def SplitTextfile(text_file):
	kkma=Kkma()
	text_data = text_file.read()
	#print text_data
	output=kkma.sentences(text_data) 
	#print output[0]

	#convert unicode to text

	return output

def SentenceExtract(file_name, topic_words):
	
	#File open
	file_name = "data/소나기.txt"
	fp = open(file_name, 'r')
	
	#Split text file to sentences 
	sentences=SplitTextfile(fp)
	#print sentences[0], sentences[0].encode('utf8'), sentences[0].decode('utf8')
	
	topic_words=['소년', '소녀', '허수아비','조약돌','스웨터']
	#Make words - sentences matrix
	score=[0 for i in range(len(sentences))]
	for word in topic_words:
		for i in range(len(sentences)):
			#print sentences[i], word, sentences[i].count(word)
			score[i]=score[i]+sentences[i].count(word)

	#print len(sentences), score
		
	#Attatch (sentence, score) and Sorting 
	for i in range(len(sentences)):
		sentences[i]=[sentences[i],score[i]]
	
	sorted_sentences = sorted(sentences, key=lambda l:l[1], reverse=True)

	for i in range(10):
		print sorted_sentences[i][0], sorted_sentences[i][1]

	#<PRINT UNICODE>
	# a = type: unicode
	# a.encode('utf8') -> 한글로 출력!

	fp.close()

SentenceExtract(0,0)

#-*- coding: utf-8 -*-

#Split text file to sentences 
#Extract sentences including topic words.

import sys
from konlpy.tag import Kkma
from konlpy.utils import pprint
import nltk.data


reload(sys)
sys.setdefaultencoding('utf-8')

#Split text file to sentences
def SplitTextfile(content):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	
	#kkma=Kkma()
	#output=kkma.sentences(content) 
	#print output[0]
	content = content.replace('다.','다.^^^' )
	output = content.split('^^^')
#	print '\n-----\n'.join(output)
#	output = join(tokenizer.tokenize(content))

	#convert unicode to text
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

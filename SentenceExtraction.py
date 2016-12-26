# -*- coding: utf-8 -*-

#Split text file to sentences 
#Extract sentences including topic words.

import sys
from konlpy.tag import Kkma
from konlpy.utils import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

#Split text file to sentences
def SplitTextfile(text_file):
	text_data = text_file.read()
	output=kkma.sentences(text_data)
	pprint(output)

	return output

def SentenceExtraction(file_name, topic_words):
	
	#file open
	file_name = "data/흥부와놀부.txt"
	fp = open(file_name, 'r')
	
	#split text file to sentences 
	sentences=SplitTextfile(fp)
	
	#make words - sentences matrix
	score=[0 for in range(len(sentences))]
	for word in topic_words:
		
		

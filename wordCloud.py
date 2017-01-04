#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Draw word Cloud from data/url.txt 's  website

from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Mecab
from lxml import html
import pytagcloud # requires Korean font support
import sys
from goose import Goose
from goose.text import StopWordsKorean

def get_bill_text():
	doc_list= []
	bloblist = []
	#The name of book is written on tran_data.txt
	f = open('./data/url.txt')
	g = Goose({'stopwords_class':StopWordsKorean})
	
	lines = f.readlines()
	f.close()
	text = ''
	for line in lines:
		text = text + g.extract(url=line).cleaned_text
  	
  	return text

def get_tags(text, ntags=50, multiplier=10):
   	mecab = Mecab()
   	nouns = mecab.nouns(text)
   	count = Counter(nouns)
   	return [{ 'color': color(), 'tag': n, 'size': c*multiplier }\
                for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

if __name__ == "__main__":
	if sys.version_info[0] >= 3:
   		urlopen = urllib.request.urlopen
	else:
		urlopen = urllib.urlopen

	r = lambda: random.randint(0,255)
	color = lambda: (r(), r(), r())

#	file = open('wordcloud.png', 'w')

	text = get_bill_text()
	tags = get_tags(text)
#	print (os.getcwd()) #현재 디렉토리의
#	print(tags)
	draw_cloud(tags, './wordcloud.png')


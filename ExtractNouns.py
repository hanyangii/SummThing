#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Twitter
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from lxml import html
import pytagcloud # requires Korean font support
import sys

from konlpy.utils import pprint
from PIL import Image
import PIL.ImageOps
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

#read from web site
def get_bill_text(new_url):
	url = new_url
	response = urlopen(url).read().decode('utf-8')
	page = html.fromstring(response)
	text = page.xpath(".//div[@id='bill-sections']/pre/text()")[0]
	return text

def get_tags(text, ntags=50, multiplier=10):
	h = Hannanum()
	nouns = h.nouns(text)
	count = Counter(nouns)
	return [{ 'color': color(), 'tag': n, 'size': c*multiplier }\
		for n, c in count.most_common(ntags)]

def get_nouns(text, chunk=500, mfv=20):
#	h = Hannanum()
#	komoran = Komoran()
#	kk = Kkma()
	tt = Twitter()
#	arr = kk.pos(text)
	arr = tt.nouns(text)
#	nngs = []

#	for i in range(len(arr)):
#		if arr[i][1] in ['Noun']: #['NNG', 'NNP']:
#			nngs.append(arr[i][0])
#pprint(nngs)		
	return arr
#	for i in range(len(arr)/chunk):
#		nngs = []
#		for j in range(chunk):
			
#			if arr[i*chunk + j][1] in ['NNG', 'NNP']:
#				nngs.append(arr[i*chunk + j][0])
	
#		count = Counter(nngs)
#		brr = count.most_common(mfv)
#		pprint(brr)
#	return brr	

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(1024, 768)):
	pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
	webbrowser.open(filename)

if __name__ == "__main__":
	if sys.version_info[0] >= 3:
		urlopen = urllib.request.urlopen
	else:
		urlopen = urllib.urlopen
		r = lambda: random.randint(0,255)
		color = lambda: (r(), r(), r())

	#####################
	###if use website ###
	#####################
	#text = get_bill_text(bill_num)


	#data_name = raw_input("type the name of article to read :")
	data_name = '소나기'
	text = read_text(data_name)
	#tags = get_tags(text)
	#print(tags)
	nouns = get_nouns(text)
#pprint(nouns)

	#######show image########
	#draw_cloud(tags, 'wordcloud.png')
	#drawImage = "wordcloud.png"
	#im = Image.open(drawImage)
	#im.show()

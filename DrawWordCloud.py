#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Hannanum
from lxml import html
import pytagcloud # requires Korean font support
import sys

from PIL import Image
import PIL.ImageOps

if sys.version_info[0] >= 3:
    urlopen = urllib.request.urlopen
else:
	urlopen = urllib.urlopen
	r = lambda: random.randint(0,255)
	color = lambda: (r(), r(), r())

#read from local file
def read_text(fileName):
	location = '/Users/jeongjiwon/SummThing/%s' %fileName
	with open(location, 'r') as f:
		doc = f.read().decode('utf-8')
	f.close()
	return doc

#read from web site
def get_bill_text(billnum):
	url = 'http://pokr.kr/bill/%s/text' % billnum
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

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
	pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
	webbrowser.open(filename)

#bill_num = '1904880'
#text = get_bill_text(bill_num)
bill_num = 'newspaper'
text = read_text(bill_num)
tags = get_tags(text)
print(tags)
draw_cloud(tags, 'wordcloud.png')

#show image
drawImage = "wordcloud.png"
im = Image.open(drawImage)
im.show()

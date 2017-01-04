#!/usr/bin/env python
# -*- coding: utf-8 -*-

from konlpy.utils import pprint
from nltk import ne_chunk

import numpy as np
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

def Analysis():
	pos_data = np.load('data/PosData.npy').tolist()
	temp=open('tmp.txt','w')
	nes=ne_chunk(pos_data, binary=False)
	pprint(nes)
	for p in pos_data: 
		temp.write(p[0] + ' '+p[1]+'\n')
		if p[0]=='김종대': pprint(p)
	#pprint(pos_data)
	url = open('data/url.txt').read()
	'''
	values={'s':text.encode('utf8')}
	article = requests.get(url, params=values)
	print article
	'''
	temp.close()
if __name__=="__main__":
	Analysis()

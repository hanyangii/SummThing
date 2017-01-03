#!/usr/bin/env python
# -*- coding: utf-8 -*-

from konlpy.utils import pprint
from konlpy.tag import Hannanum
import pumsaWord

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 
han = Hannanum()

sentence = u'" 저 녀석은 무슨 일을 시키면 언제나 거꾸로 한단 말 야. 엄마 개구리는 죽으면서 청개구리에게 말했어요.'
result = []
result = han.analyze(sentence)

joo_eo = []
sool_eo = []
mog_eo = []
bo_eo = []


pprint(result)
pre_word = ''
neg_word = ''

for i in range(len(result)):
	if(not len(result[i])):
		continue
	p = pumsaWord.Pumsa(result[i][0])
	word = pumsaWord.FullWord(result[i][0])		         
	word = pre_word + word
	pre_word = ''

	print(word + "pumsa : ")
	print(p)

	if (p == 2 and neg_word != ''):
		word = neg_word + word
		neg_word = ''

	if p == 1:  #S
		joo_eo.append(word)

	elif p == 2: #V
		sool_eo.append(word)

	elif p == 3: #O
		mog_eo.append(word)

	elif p == 4: #C
		bo_eo.append(word)

	elif p == 5: #A
		pre_word = pre_word + word + ' '

	if (word in ['안', '못']):
		neg_word = word + ' '

print('\n**************************')
print('S:')
for i in range(len(joo_eo)):
    pprint(joo_eo[i])
print('**************************')
print('V:')
for i in range(len(sool_eo)):
	pprint(sool_eo[i])	
print('**************************')
print('O:')
for i in range(len(mog_eo)):
	pprint(mog_eo[i])
print('**************************')
print('C:')
for i in range(len(bo_eo)):
	pprint(bo_eo[i])										           

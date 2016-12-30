# -*- coding: utf-8 -*-
#!/usr/bin/env python

from konlpy.utils import pprint
from konlpy.tag import Hannanum
import pumsaWord
#import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

han = Hannanum()

sentence = u'aaaaa.'
result = []
result = han.analyze(sentence)

joo_eo = []
sool_eo = []
mog_eo = []
bo_eo = []


#pprint(result)

for i in range(len(result)):
    p = pumsaWord.Pumsa(result[i][0])
    word = pumsaWord.FullWord(result[i][0])
      
    if p == 1:  #주어일때
        joo_eo.append(word)

    elif p == 2: #서술어일때
        sool_eo.append(word)

    elif p == 3: #목적어일때
        mog_eo.append(word)

    elif p == 4: #보어일때
        bo_eo.append(word)

print('\n**************************')
print('옜:')
for i in range(len(joo_eo)):
    pprint(joo_eo[i])
print('**************************')
print('서술어:')
for i in range(len(sool_eo)):
    pprint(sool_eo[i])
print('**************************')
print('목적어:')
for i in range(len(mog_eo)):
    pprint(mog_eo[i])
print('**************************')
print('보어:')
for i in range(len(bo_eo)):
    pprint(bo_eo[i])
        

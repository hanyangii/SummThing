# -*- coding: ms949 -*-

from konlpy.utils import pprint
from konlpy.tag import Hannanum
import pumsaWord
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

han = Hannanum()

#print(han.analyze(u'본 연구의 목적은 통일된 한국어 품사태그 집합을 설정하는 데 있다.'))
#konlpy.utils.pprint(han.analyze(u'본 연구의 목적은 통일된 한국어 품사태그 집합을 설정하는 데 있다.'))

sentence = u'이 테스트 문장은 주어와 목적어를 구분하기 위한 샘플이다.'
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
print('주어:')
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
        

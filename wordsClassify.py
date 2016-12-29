# -*- coding: ms949 -*-

from konlpy.utils import pprint
from konlpy.tag import Hannanum
import pumsaWord
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

han = Hannanum()

#print(han.analyze(u'�� ������ ������ ���ϵ� �ѱ��� ǰ���±� ������ �����ϴ� �� �ִ�.'))
#konlpy.utils.pprint(han.analyze(u'�� ������ ������ ���ϵ� �ѱ��� ǰ���±� ������ �����ϴ� �� �ִ�.'))

sentence = u'�� �׽�Ʈ ������ �־�� ����� �����ϱ� ���� �����̴�.'
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
      
    if p == 1:  #�־��϶�
        joo_eo.append(word)

    elif p == 2: #�������϶�
        sool_eo.append(word)

    elif p == 3: #�������϶�
        mog_eo.append(word)

    elif p == 4: #�����϶�
        bo_eo.append(word)

print('\n**************************')
print('�־�:')
for i in range(len(joo_eo)):
    pprint(joo_eo[i])
print('**************************')
print('������:')
for i in range(len(sool_eo)):
    pprint(sool_eo[i])
print('**************************')
print('������:')
for i in range(len(mog_eo)):
    pprint(mog_eo[i])
print('**************************')
print('����:')
for i in range(len(bo_eo)):
    pprint(bo_eo[i])
        

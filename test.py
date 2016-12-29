# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Hannanum
from konlpy.tag import Komoran
import datetime
print(str(datetime.datetime.now()))
print("===============komoran=====================")
komoran = Komoran()
#pprint(komoran.pos(u'우왕 코모란도 오픈소스가 되었어요'))
#pprint(komoran.pos(u'원칙이나 기체 설계와 엔진·레이더·항법장비 등'))
pprint(komoran.pos(u'다람쥐 헌 쳇바퀴에 타고파'))
print(str(datetime.datetime.now()))

print("===============kkma=====================")
kkma = Kkma()
pprint(kkma.pos(u'다람쥐 헌 쳇바퀴에 타고파'))

print(str(datetime.datetime.now()))
print("===============twitter=====================")
twitter = Twitter()
pprint(twitter.pos(u'다람쥐 헌 쳇바퀴에 타고파', norm=True, stem=True))

#mecab = Mecab()
#pprint(kkma.pos(u'mecab: 백설공주는 독사과를 먹고 죽었다.'))

print(str(datetime.datetime.now()))
print("===============hannanum=====================")
h = Hannanum()
pprint(h.pos(u'다람쥐 헌 쳇바퀴에 타고파'))
print(str(datetime.datetime.now()))


# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Hannanum
from konlpy.tag import Komoran

kkma = Kkma()
pprint(kkma.pos(u'kkma: 백설공주는 독사과를 먹고 죽었다.'))


twitter = Twitter()
pprint(twitter.pos(u'twitter: 백설공주는 독사과를 먹고 죽었다', norm=True, stem=True))

#mecab = Mecab()
#pprint(kkma.pos(u'mecab: 백설공주는 독사과를 먹고 죽었다.'))


hannanum = Hannanum()
pprint(kkma.pos(u'hannanum: 백설공주는 독사과를 먹고 죽었다.'))



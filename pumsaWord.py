# -*- coding: utf-8 -*-
#!/usr/bin/env python

from konlpy.utils import pprint

def Pumsa(words):
    pprint(words)
    first = words[0][1]
    last = words[len(words) - 1][1] #단어를 형태소 단위로 분리했을 때 마지막 품사
    ans = 0

    #S
    if (last in ['jcs', 'jxc']):
        ans = 1

    #V
    elif (last == 'ef'):
        ans = 2
        
    elif (first in ['pvd','pvg']):
        ans = 2

    #O
    elif (last == 'jco'):
        ans = 3

    #C
    elif (last == 'jcc'):
        ans = 4
	
	#A
    elif (last == 'jcm'):
	    ans = 5

    return ans

def FullWord(words):
    full = ""
    for i in range(len(words)):
        full += words[i][0]

    return full
    

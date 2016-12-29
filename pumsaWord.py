# -*- coding: ms949 -*-

from konlpy.utils import pprint

def Pumsa(words):
    pprint(words)
    last = words[len(words) - 1][1] #단어를 형태소 단위로 분리했을 때 마지막 품사
    ans = 0

    #주어
    if (last == 'jcs' or last == 'jxc'):
        ans = 1

    #서술어
    elif (last == 'ef'):
        ans = 2

    #목적어
    elif (last == 'jco'):
        ans = 3

    #보어
    elif (last == 'jcc'):
        ans = 4

    return ans

def FullWord(words):
    full = ""
    for i in range(len(words)):
        full += words[i][0]

    return full
    

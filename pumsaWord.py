# -*- coding: ms949 -*-

from konlpy.utils import pprint

def Pumsa(words):
    pprint(words)
    last = words[len(words) - 1][1] #�ܾ ���¼� ������ �и����� �� ������ ǰ��
    ans = 0

    #�־�
    if (last == 'jcs' or last == 'jxc'):
        ans = 1

    #������
    elif (last == 'ef'):
        ans = 2

    #������
    elif (last == 'jco'):
        ans = 3

    #����
    elif (last == 'jcc'):
        ans = 4

    return ans

def FullWord(words):
    full = ""
    for i in range(len(words)):
        full += words[i][0]

    return full
    

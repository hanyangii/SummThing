#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk import collocations
from konlpy.tag import Kkma

import numpy as np
import sys

from ExtractNouns import *

reload(sys)
sys.setdefaultencoding('utf-8')

def find_NNpairs(score_words):
    find_words = ['NNG', 'NNP']
    collocs = []
    word_pairs = []
    for pair in score_words:
        if pair[0][0][1] in find_words and pair[0][1][1] in find_words:
            if pair[1] > 25.0:
                collocs.append(pair)
                pp = [pair[0][0][0], pair[0][1][0]]
                word_pairs.append(pp)
    return word_pairs

def get_collocation_pairs(article, data_save_file):
    nouns = get_nouns(article)
    measures = collocations.BigramAssocMeasures()
    tagged_words = Kkma().pos(article)

    if data_save_file != False:
        np.save(data_save_file, tagged_words)
    finder = collocations.BigramCollocationFinder.from_words(tagged_words)
    score_words = finder.score_ngrams(measures.likelihood_ratio)

    word_pairs = find_NNpairs(score_words)

    return word_pairs
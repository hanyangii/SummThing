# -*- coding: utf-8 -*-

import sys
from TF_IDF import *
from SentenceExtraction import *

reload(sys)
sys.setdefaultencoding('utf-8')

#train every train data
topic_words = TF_IDF_url()

#topic_words = TF_IDF()
Extraction(topic_words)

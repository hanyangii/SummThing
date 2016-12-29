#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb


def tf(word, blob):
	print(blob.words.count(word) , len(blob.words))
	return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
	return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
									 
def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)

	
document1 = tb("""소년은 개울가에서 소녀를 보자 곧 윤 초시네 증손녀(曾孫女)딸이라는 걸 알 수 있었다. 
		소녀는 개울에다 손을 잠그고 물장난을 하고 있는 것이다. 서울서는 이런 개울물을 보지 못하기나 한 듯이.
		벌써 며칠째 소녀는, 학교에서 돌아오는 길에 물장난이었다. 그런데, 
		어제까지 개울 기슭에서 하더니, 오늘은 징검다리 한가운데 앉아서 하고 있다.
		소년은 개울둑에 앉아 버렸다. 소녀가 비키기를 기다리자는 것이다.
		이 날은 소녀가 징검다리 한가운데 앉아 세수를 하고 있었다. 
		분홍 스웨터 소매를 걷어올린 목덜미가 마냥 희었다.
		한참 세수를 하고 나더니, 이번에는 물 속을 빤히 들여다 본다. 
		얼굴이라도 비추어 보는 것이리라. 갑자기 물을 움켜 낸다. 고기 새끼라도 지나가는 듯.
		소녀는 소년이 개울둑에 앉아 있는 걸 아는지 모르는지 그냥 날쌔게 물만 움켜 낸다.""")

document2 = tb("""Python, from the Greek word (πύθων/πύθωνας), is a genus of
	nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
	recognised.[2] A member of this genus, P. reticulatus, is among the longest
	snakes known.""")

document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
	manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
	It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
	in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
	Colt Python targeted the premium revolver market segment. Some firearm
	collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
	Thompson, Renee Smeets and Martin Dougherty have described the Python as the
	finest production revolver ever made.""")

bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
	print("Top words in document {}".format(i + 1))
	scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	for word, score in sorted_words[:3]:
		print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


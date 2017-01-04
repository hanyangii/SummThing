#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import datetime
import newspaper
import urllib
import sys

from TF_IDF import *
from NewsCrawlling import *

reload(sys)
sys.setdefaultencoding('utf-8')

GOOGLE_PREFIX="https://news.google.com/news/story?ncl=dpKqTn72qkbAbrMW-51QrGE_LZjHM&q="
GOOGLE_POSTFIX="&lr=Korean&hl=ko&sa=X&ved=0ahUKEwjJ0a_O16fRAhXBrJQKHSIqBAcQqgIIJDAA"

def construct_Article_class(title,url,date):
	ArticleClass=Textdoc()
	ArticleClass.save_article(title,url,date)
	
	return ArticleClass

#Return related articles list
def search_news(word_list):
	search_line = ""
	for word in word_list:
		search_line=search_line+word
		if word_list.index(word) == len(word_list)-1 : break
		search_line=search_line+'+'
	
	url = GOOGLE_PREFIX+search_line+GOOGLE_POSTFIX
	print url
	soup = get_source(url)
	article_link =[]

	for article in soup.find_all('div',{'class':'thumbnail'}):
		tit_link = article.select('a')
		if(len(tit_link)>0):
			link = tit_link[0]['href']
		#Extract Article
		print link
		news=newspaper.Article(link,language='ko')
		news.download()
		try:
			news.parse()
		except:
			continue

		title = news.title
		print title
		date = news.publish_date
		if not date:
			date = datetime.date(0001,01,01)
		article_class = construct_Article_class(title,link,date)
		article_link.append(article_class)

	return article_link

if __name__=='__main__':
	WordsFile = open('data/writeWord.txt','r')
	ArticleFile = open('data/RelatedArticles.txt','w')
	words=[]
	while True:
		line = WordsFile.readline().split('\n')[0]
		if not line : break
		words.append(line)
	articles=search_news(words)

	for article in articles:
		title, date, url = article.pop_article()
		date = date.isoformat()
		print title
		if len(title)>0: ArticleFile.write(title+' '+date+' '+url+'\n')

	WordsFile.close()
	ArticleFile.close()


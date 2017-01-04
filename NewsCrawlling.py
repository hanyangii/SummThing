# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import datetime
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

URL_PREFIX = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date="

#Crawling URLs from NAVER news pages
def get_link(access_url):
    source_from_url = urllib.urlopen(access_url)
    soup = BeautifulSoup(source_from_url, 'lxml', from_encoding='utf-8')
    links=[]
    for article in soup.find_all('dt'):
        tit_link = article.select('a')
        if(len(tit_link)>0):
            post_fix=tit_link[0]['href']
            if post_fix.split(':')[0]=='http' : url = post_fix
            else: url = "http://news.naver.com"+post_fix
            #print url
            links.append(url)
            #print url

    return links

#append new urls in list
def merge_links(link_list, links):
    for link in links:
        link_list = link_list + link + '\n'

    return link_list

#make 6 news parts' urls
def get_urls():
    link_list=""
    today = datetime.date.today().toordinal()

    for week in range(1,53):
        fine_date=datetime.date.fromordinal(today-week*7)

        #print fine_date
        date_format=fine_date.isoformat()
        date_format=date_format.split('-')
        date_format=date_format[0]+date_format[1]+date_format[2]
        crawl_url=URL_PREFIX+date_format

        #print crawl_url
        n_links=get_link(crawl_url)
        link_list=merge_links(link_list,n_links)

    return link_list

if __name__ == '__main__':
    TrainFile = open('data/train_articles.txt','w')
    TrainFile.write(get_urls())
    TrainFile.close()

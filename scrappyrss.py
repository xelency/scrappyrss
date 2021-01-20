# scrapping engine

import requests
from bs4 import BeautifulSoup
import lxml

# scraping function
def run_rss(target_rss):
	article_list = []
	try:
		r = requests.get(target_rss)
		soup = BeautifulSoup(r.content, features='xml')
		articles = soup.findAll('item')
		for a in articles:
			title = a.find('title').text
			link = a.find('link').text
			pubdate = a.find('pubDate').text
			article = {
			'title': title,
			'link': link,
			'published': pubdate
			}
			article_list.append(article)
		return print(article_list)
	except Exception as e:
		print('The scraping job failed. See exception: ')
		print(e)
print('Starting scraping')
run_rss('https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine.rss')
print('Finished scraping')
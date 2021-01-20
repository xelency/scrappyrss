# scrapping engine

import requests
from bs4 import BeautifulSoup

# scraping function
def run_rss(target_rss):
    try:
        r = requests.get(target_rss)
        return print('The scraping job succeeded: ', r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
print('Starting scraping')
run_rss('https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine.rss')
print('Finished scraping')
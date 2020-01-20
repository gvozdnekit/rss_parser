import feedparser
from bs4 import BeautifulSoup
import os
import json
import datetime

import time

def cleanHTML(html):
    if html == '': return ''

    return BeautifulSoup(html, 'html5lib').get_text()


def read_news():
    currentDate = str(datetime.datetime.now().date())
    feed_link = 'http://factmil.com/news/rss/'
    out_file = os.path.join('Новости на ' + currentDate + '.json')

    d = feedparser.parse(feed_link)
    print(d)
    fact_mil_news = []
    for i in d.entries:
        fact_mil_news.append({'title': i.title,
                              'date': i.published,
                              'context': cleanHTML(i.content[0].value),
                              'link': i.link,
                              'tag': i.tags[0].term})

    with open(out_file, 'w', encoding='utf-8') as f:

        json.dump(fact_mil_news, f, ensure_ascii=False, indent=4)
        print('Записал')


while True:
    read_news()
    time.sleep(86400)

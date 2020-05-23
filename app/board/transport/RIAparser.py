import bs4
import re
import time
import string
import requests
import random
import numpy as np

from .Transport import Transport


class RIAparser(Transport):

    def __init__(self):
        self.articles = []
        letters = string.ascii_letters
        self.agent = ''.join(random.choices(letters, k=np.random.randint(9, 15)))
        self.headers = {'Referer': 'https://ria.ru',
                        'User-Agent': self.agent}

    def get(self, tag, n=20, **params):
        try:
            n_offsets = params['offset']
        except:
            n_offsets = None
        for i in range(n_offsets):
            print('Offset',i)
            hrefs = self.get_hrefs(tag=tag,
                                   request_params={'offset': i * 20},
                                   headers=self.headers)
            for href in hrefs[:n]:
                try:
                    article_info = self.get_article_info(href, headers=self.headers)
                    self.articles.append(article_info)
                    time.sleep(np.random.randint(1, 3) / 2.1)
                except Exception as e:
                    print(e)
                    continue
        return self.articles

    @staticmethod
    def get_hrefs(tag,
                  request_params={},
                  headers={'User-agent': 'My agent'},
                  base_url='https://ria.ru/search/') -> list:

        params = {'query': tag}
        params = dict(params, **request_params)
        r = requests.get(url=base_url, params=params, headers=headers)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        hrefs = soup.find_all('a', attrs={'class': 'list-item__image'})

        return [x['href'] for x in hrefs]

    @staticmethod
    def get_article_info(href, headers={'User-agent': 'My agent'}) -> dict:
        article = requests.get(href, headers=headers)
        article = bs4.BeautifulSoup(article.text, 'lxml')

        title = article.find('h1', attrs={'class': 'article__title'})
        title = title.text

        body = article.find_all('div', attrs={'class': 'article__text'})
        text = ''.join([x.text for x in body])

        created_at = article.find('div', attrs={'class': 'article__info-date'})
        reg = "\d\d\.\d\d\.\d\d\d\d"
        date = re.findall(reg, created_at.text)
        created_at = date[-1]
        return dict(title=title,
                    text=text,
                    created_at=created_at)

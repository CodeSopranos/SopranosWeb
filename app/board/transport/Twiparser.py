from .Transport import Transport
from twitter_scraper import get_tweets, get_trends


class TWITTERparser(Transport):

    def __init__(self):
        self.articles = []

    def get(self, tag, n=5, **params) -> list:
        for tweet in get_tweets(tag, pages=n):
            self.articles.append({'title': tweet['username'],
                                  'created_at': str(tweet['time']),
                                  'text': tweet['text'],
                                  'likes': tweet['likes'],
                                  'replies': tweet['replies']})
        return self.articles
    def get_trends_tags(self) -> list:
        return get_trends()

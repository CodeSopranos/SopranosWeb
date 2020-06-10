import pymorphy2
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from .Analyzer import Analyzer
morph = pymorphy2.MorphAnalyzer()

class Frequency(Analyzer):

    def __init__(self, articles):
        self.articles = articles

    def preprocess(self):
        info_dct = {'title': [], 'text': [], 'created_at': []}
        for article in self.articles:
            info_dct['title'] += [article['title']]
            info_dct['text'] += [article['text']]
            info_dct['created_at'] += [article['created_at']]
        self.df = pd.DataFrame.from_dict(info_dct)
        self.df['text'] = self.df['text'].apply(lambda x: self.clean(x))

    def analyze(self):
        vectorizer = CountVectorizer(max_df=0.5)
        X = vectorizer.fit_transform(self.df['text'])
        count_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
        freq = count_df.sum()
        freq_dct = {k:freq[k] for k in sorted(dict(freq), key=lambda x: freq[x])}
        return freq.sort_values(ascending=False)[:15]

    @staticmethod
    def clean(data):
        try:
            index = data.index('.')
            data = data[index:]
        except:
            pass
        words = []
        for word in data.split(' '):
            flag = True
            if flag:
                parsed = morph.parse(word)
                if 'NOUN' in parsed[0].tag:
                    words.append(parsed[0].normal_form)
        return ' '.join(words)


    @staticmethod
    def clean_eng(data):
        try:
            index = data.index('.')
            data = data[index:]
        except:
            pass
        words = []
        for word in data.split(' '):
            words.append(parsed[0].normal_form)
        return ' '.join(words)

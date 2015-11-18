import MeCab
import glob
import codecs
import re
import numpy as np
import sys
sys.path.append("./components/")
from component import component
sys.path.append("./models/")
from articles import articles

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

class autotagcompo(component):
    def setup(self):
        self.max_df = 100
        self.min_df = 5
        self.min_tfidf = 0.10
        self.max_features = 10000
        self.articles = articles()

    def __tokenize(self, text):
        """ MeCab で分かち書きした結果をトークンとして返す """
        wakati = MeCab.Tagger("-O wakati")
        return wakati.parse(text)

    def __split(self, text):
        return text.split()

    def make_tags_with_new_text(self, text):
        texts = [item[1] for item in self.articles.find_all()]
        texts.append(text)
        vectorizer = TfidfVectorizer(
            max_df=self.max_df,
            min_df=self.min_df,
            analyzer=self.__split,
            tokenizer=self.__tokenize,
            max_features=self.max_features,
            stop_words=' '
            )
        X = vectorizer.fit_transform(texts)
        terms = vectorizer.get_feature_names()
        tags_list = []
        x = X.toarray()
        tfidfs = x[-1]
        tags_list.append([term for term in terms if tfidfs[terms.index(term)] > self.min_tfidf])
        return tags_list
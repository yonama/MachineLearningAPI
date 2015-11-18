import MeCab
import glob
import codecs
import re
import sys
sys.path.append("./components/")
from component import component

class nominalization(component):
    def setup(self):
        self.mecab = MeCab.Tagger('mecabrc')
        self.symbol = re.compile("[!-/:-@[-`{-~<>#a-zA-Z0-9]")

    def __get_nouns(self, text):
        self.mecab.parse('')
        node = self.mecab.parseToNode(text)
        while node:
            if node.feature.split(',')[0] == '名詞':
                surface = node.surface
                token = re.sub(self.symbol, '', surface)
                if token != '':
                    yield token
            node = node.next
        raise StopIteration

    def nominalization(self, text):
        result = ""
        for item in self.__get_nouns(text):
            result = result + " " + item
        return result

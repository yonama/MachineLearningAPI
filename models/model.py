#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import glob
import os.path
import codecs
import re

class model(object):
    __metaclass__ = ABCMeta

    def set_data(self, id, data=None):
        self.__id = str(id)
        self.__data = data

    def find_all(self):
        for file in glob.glob('./models/resources/' + self.__class__.__name__ + '/*'):
            id = re.compile("[0-9]+").search(file).group(0)
            allLines = open(file, 'r', encoding='utf-8').read()
            self.set_data(id, allLines)
            yield (id, allLines)

    def find(self, id):
        file = './models/resources/' + self.__class__.__name__ + '/' + str(id)
        print(file)
        if os.path.isfile(file):
            allLines = open(file, 'r', encoding='utf-8').read()
            self.set_data(id, allLines)
            return (id, allLines)
        else:
            return (id, None)

    #data -> value
    def save(self, data):
        file = 'resources/' + self.__class__.__name__ + '/' + str(self.__id)
        f = codecs.open(file, 'w', 'utf-8')
        f.write('%s' % data)

    #data -> [(id, value)]
    #def save(self, List data):
    #    for datum in data:
    #        self.set_data(datum[0])
    #        self.save(datum[1])

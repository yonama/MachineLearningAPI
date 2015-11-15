#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sys
sys.path.append("./controllers/filters/")
from filters.filter import filter

#抽象化してデコレータを定義だけしとく
class controller(object):
    __metaclass__ = ABCMeta
    exposed = True
    def __init__(self):
        self.filter = filter(self)
        self.setup()

    def setup(self):
        pass

    @abstractmethod
    def befour_action(self):
        raise NotImplementedError()

    @abstractmethod
    def after_action(self):
        raise NotImplementedError()

    @abstractmethod
    def around_action(self):
        raise NotImplementedError()

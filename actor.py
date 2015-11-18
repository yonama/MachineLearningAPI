#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sys
from filters.filter import filter

class actor(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.filter = filter(self)
        self.setup()

    def setup(self):
        pass

    #これいらないかも
    @abstractmethod
    def befour_action(self):
        raise NotImplementedError()
    @abstractmethod
    def after_action(self):
        raise NotImplementedError()
    @abstractmethod
    def around_action(self):
        raise NotImplementedError()

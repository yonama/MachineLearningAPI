#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from actor import actor
from filters.controller_filter import controller_filter as filter

#抽象化してデコレータを定義だけしとく
class controller(actor):
    exposed = True

    def setup(self):
        self.filter = filter(self)

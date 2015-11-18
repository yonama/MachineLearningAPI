#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from actor import actor
from filters.component_filter import component_filter as filter

class component(actor):
    def setup(self):
        self.filter = filter(self)

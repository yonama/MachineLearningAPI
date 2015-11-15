#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class filter(object):
    __metaclass__ = ABCMeta

    def __init__(self, delegate):
        self.delegate = delegate

    def befour_filter(self):
        def _befour_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.befour_action()
                result = func(*args, **kwds)
                return result
            return new_func
        return _befour_filter

    def after_filter(self):
        def _after_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                result = func(*args, **kwds)
                self.delegate.after_action()
                return result
            return new_func
        return _after_filter

    def around_filter(self):
        def _around_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.befour_action()
                result = func(*args, **kwds)
                self.delegate.after_action()
                return result
            return new_func
        return _around_filter

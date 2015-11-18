#!/usr/bin/env python
# -*- coding: utf-8 -*-
from filters.filter import filter

class model_filter(filter):
    def save_befour_filter(self):
        def _save_befour_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.save_befour_action()
                result = func(*args, **kwds)
                return result
            return new_func
        return _save_befour_filter

    def save_after_filter(self):
        def _save_after_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                result = func(*args, **kwds)
                self.delegate.save_after_action()
                return result
            return new_func
        return _save_after_filter

    def save_around_filter(self):
        def _save_around_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.save_befour_action()
                result = func(*args, **kwds)
                self.delegate.save_after_action()
                return result
            return new_func
        return _save_around_filter

    def find_befour_filter(self):
        def _find_befour_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.find_befour_action()
                result = func(*args, **kwds)
                return result
            return new_func
        return _find_befour_filter

    def find_after_filter(self):
        def _find_after_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                result = func(*args, **kwds)
                self.delegate.find_after_action()
                return result
            return new_func
        return _find_after_filter

    def find_around_filter(self):
        def _find_around_filter(func):
            from functools import wraps
            @wraps(func)
            def new_func(*args, **kwds):
                self.delegate.find_befour_action()
                result = func(*args, **kwds)
                self.delegate.find_after_action()
                return result
            return new_func
        return _find_around_filter

#!/usr/bin/env python3
"""Basic dictionary Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system class """
    def put(self, key, item):
        """ Put data in cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get data from cache """
        if key in self.cache_data.keys():
            return self.cache_data[key]

        return None

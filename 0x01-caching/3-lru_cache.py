#!/usr/bin/env python3
"""LRU caching Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching class """

    def __init__(self):
        """ Initialize LRU class """
        super().__init__()

    def put(self, key, item):
        """ Put data in cache """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) == self.MAX_ITEMS:
                if key in self.cache_data.keys():
                    self.cache_data[key] = item
                    # print("Discard: {}".format(key))
                else:
                    last_key = sorted(self.cache_data.keys())[-1]
                    del self.cache_data[last_key]
                    print("Discard: {}".format(last_key))
                    self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get data from cache """
        if key in self.cache_data.keys():
            return self.cache_data[key]

        return None

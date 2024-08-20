#!/usr/bin/env python3
"""FIFO caching Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching class """

    def __init__(self):
        """ Initialize FIFO class """
        super().__init__()

    def put(self, key, item):
        """ Put data in cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("Discard: {}".format(first_key))
    
    def get(self, key):
        """ Get data from cache """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        
        return None

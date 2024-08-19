#!/usr/bin/env python3
""" Helper function module
"""


def index_range(page, page_size):
    """ Calculate index range """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

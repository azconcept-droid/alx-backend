#!/usr/bin/env python3
""" Hypermedia pagination module
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        pages = []
        for data in self.dataset()[start_index:]:
            if start_index == end_index:
                break
            pages.append(data)
            start_index += 1

        return pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get hypermedia pagination """
        hyper = {}
        hyper["page_size"] = page_size
        hyper["page"] = page
        hyper["data"] = self.get_page(page, page_size)
        hyper["next_page"] = page + 1
        hyper["prev_page"] = None if (page - 1 == 0) else page - 1
        hyper["total_pages"] = len(self.dataset())
        return hyper


def index_range(page: int, page_size: int) -> Tuple:
    """ Calculate index range """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

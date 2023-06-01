#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        pass
    def get_title(self):
        return self._title
    def get_page_count(self):
        return self._page_count
    def set_title(self, title):
        self._title = title
        pass
    def set_page_count(self, page_count):
        self._page_count = page_count if isinstance(page_count, int) else print("page_count must be an integer")
        pass
    title = property(get_title, set_title)
    page_count = property(get_page_count, set_page_count)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    pass
    
         
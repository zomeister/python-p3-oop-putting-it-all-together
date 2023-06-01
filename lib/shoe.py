#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        pass
    def get_brand(self):
        return self._brand
    def get_size(self):
        return self._size
    def set_brand(self, brand):
        self._brand = brand if isinstance(brand, str) else print("no")
        pass
    def set_size(self, size):
        self._size = size if isinstance(size, int) else print("size must be an integer")
        pass
    
    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
        pass
    
    pass
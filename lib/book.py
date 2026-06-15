#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    @property   #setting the getter
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = value
            

# book1 = Book("book1", "two")
# print(f"{book1.page_count}")
    
        
    
        
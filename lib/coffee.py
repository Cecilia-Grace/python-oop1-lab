#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        allowed_sizes = ("Large", "Medium", "Small")
        if value not in allowed_sizes:
            print("size must be Small, Medium, or Large")
            self._size = None
        else:
            self._size = value
            
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price +=1
        
coffee1 = Coffee("Larger", 20)
print(f"{coffee1.size}")
print(coffee1.tip())
print(coffee1.price)
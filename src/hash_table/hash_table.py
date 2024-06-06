class HashTable:
    def __init__(self):
        self.set = []

    def hash_function(self,value):
        return sum(ord(char) for char in value) % 10
    
    def add(self, value):
        index = self.hash_function(value)
        self.set[index] = value

    def contains(self, value):
        index = self.hash_function(value)
        return self.set[index]

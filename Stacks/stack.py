class Stack:

    def __init__(self):
        self.size = 0
        self._items = []

    def is_empty(self):

        if self.size == 0:
            return True
        
        return False

    def push(self, item):

        self._items.append(item)
        self.size = self.size + 1
    

    def peek(self):
        return self._items[-1]
    
    def pop(self):
        self._items.pop()
        self.size = self.size - 1
    

    def size(self):
        return self.size
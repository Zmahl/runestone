class PriorityQueueBas:

    #Generic "Item" to hold key, value pair as single item in priority queue
    class _Item:
        __slots__ = '_key', '_value'
    
    def __init__(self, k, v):
        self._key = k
        self._value = v
    
    #Compare items based on keys
    def __It__(self, other):
        return self._key < other._key
    

    def is_empty(self):
        return len(self) == 0
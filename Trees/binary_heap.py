#Implementation of BinaryHeap on an array 

from heapq import heapify


class BinaryHeap:
    def __init__(self):
        self._heap = []
    
    def insert(self, value):
        self._heap.append(value)
        #Calls the index of the last item in the array
        self._perc_up(len(self._heap) - 1)
    

    def _perc_up(self, current_index):

        #_perc_up will split the index in half to check the child in relation to the parent
        while (current_index - 1) // 2 >= 0:
            parent_index = (current_index - 1) // 2

            #If that child is smaller than the current parent, swap the two values
            if self._heap[current_index] < self._heap[parent_index]:
                self._heap[current_index], self._heap[parent_index] = (
                    self._heap[parent_index],
                    self._heap[current_index]
                )

        #Divide the current index by 2 again to get to the next parent within the array
        current_index = parent_index
    
    def _perc_down(self, current_index):
        while 2 * current_index + 1 < len(self._heap):
            min_child_index = self._get_min_child(current_index)
            if self._heap[current_index] > self._heap[min_child_index]:
                self._heap
    

    def get_min_child(self, parent_index):
        if 2 * parent_index + 2 > len(self._heap) - 1:
            return 2 * parent_index + 1
        
        if self._heap[2 * parent_index + 1] < self._heap[2 * parent_index + 2]:
            return 2 * parent_index + 1
        
        return 2 * parent_index + 2

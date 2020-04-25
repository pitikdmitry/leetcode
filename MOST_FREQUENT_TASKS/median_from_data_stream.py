from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        #   max heap for values < median value
        self._left_heap = PriorityQueue()
        #   min heap for values > median value
        self._right_heap = PriorityQueue()
        self._median_value = float('inf')

    def _balance(self):
        if self._left_heap.qsize() - self._right_heap.qsize() > 1:
            #   if left heap is bigger we put median value to right heap and extract new median from left heap
            self._right_heap.put((self._median_value, self._median_value))
            self._median_value = self._left_heap.get()[1]
        elif self._right_heap.qsize() - self._left_heap.qsize() > 1:
            #   if right heap is bigger we put median value to left heap and extract new median from right heap
            self._left_heap.put((-self._median_value, self._median_value))
            self._median_value = self._right_heap.get()[1]

    def addNum(self, num: int) -> None:
        if self._median_value == float('inf'):
            self._median_value = num
        elif num <= self._median_value:
            self._left_heap.put((-num, num))
        else:
            #   store to right heap with opposite sign to build max heap
            self._right_heap.put((num, num))

        self._balance()

    def findMedian(self) -> float:
        if self._left_heap.qsize() == self._right_heap.qsize():
            if self._median_value == float('inf'):
                return 0
            return self._median_value
        elif self._left_heap.qsize() > self._right_heap.qsize():
            left_heap_top = self._left_heap.get()[1]
            self._left_heap.put((-left_heap_top, left_heap_top))
            return (self._median_value + left_heap_top) / 2
        else:
            right_heap_top = self._right_heap.get()[1]
            self._right_heap.put((right_heap_top, right_heap_top))
            return (self._median_value + right_heap_top) / 2


finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print(finder.findMedian())
finder.addNum(3)
print(finder.findMedian())



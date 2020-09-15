'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
'''
import heapq


#   we use two heaps for finding median
class MedianFinder:
    def __init__(self) -> None:
        #   max heap for values < median value
        self.max_h = []
        #   min heap for values > median value
        self.min_h = []

    def _balance(self) -> None:
        #   we need two heaps of equal size or max_heap bigger by one element
        if len(self.min_h) > len(self.max_h):
            val = heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, -val)
        elif len(self.max_h) - len(self.min_h) > 1:
            val = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, -val)

    def addNum(self, num: int) -> None:
        if len(self.max_h) == 0 or num <= -self.max_h[0]:
            heapq.heappush(self.max_h, -num)
        else:
            heapq.heappush(self.min_h, num)

        self._balance()

    def findMedian(self) -> float:
        if len(self.max_h) == 0 and len(self.min_h) == 0:
            return -1
        elif len(self.max_h) == len(self.min_h):
            return (-self.max_h[0] + self.min_h[0]) / 2
        else:
            return -self.max_h[0]


finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print(finder.findMedian())
finder.addNum(3)
print(finder.findMedian())

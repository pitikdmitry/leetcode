'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
'''


import heapq
from typing import List


#   We use two heaps to maintain median inside sliding window
class Solution:
    def __init__(self) -> None:
        #   heap for storing values <= median
        self.max_h = []
        #   heap for storing values > median
        self.min_h = []

    def _balance(self) -> None:
        #   we need two heaps of equal size or max_heap bigger by one element
        if len(self.min_h) > len(self.max_h):
            val = heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, -val)
        elif len(self.max_h) - len(self.min_h) > 1:
            val = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, -val)

    def insert(self, num: int) -> None:
        if len(self.max_h) == 0 or num <= -self.max_h[0]:
            heapq.heappush(self.max_h, -num)
        else:
            heapq.heappush(self.min_h, num)

        self._balance()

    def delete(self, val: int) -> None:
        #   as we have sliding window, we need to delete elements, when we shrink window
        #   choose heap
        heap = self.min_h
        if val <= -self.max_h[0]:
            heap = self.max_h
            val = -val

        #   find element in heap
        idx = heap.index(val)
        #   change it with last element in heap
        heap[idx], heap[len(heap) - 1] = heap[len(heap) - 1], heap[idx]
        heap.pop()

        #   find position of element in heap
        if idx < len(heap):
            heapq._siftup(heap, idx)
        self._balance()

    def median(self) -> float:
        if len(self.max_h) == 0 and len(self.min_h) == 0:
            return -1
        elif len(self.max_h) == len(self.min_h):
            return (-self.max_h[0] + self.min_h[0]) / 2
        else:
            return -self.max_h[0]

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(len(nums)):
            #   add new element
            self.insert(nums[i])

            #   delete element, which is out of window
            if i >= k:
                self.delete(nums[i - k])

            #   find median
            if i >= k - 1:
                result.append(self.median())
        return result


solution = Solution()
nums = [7,0,3,9,9,9,1,7,2,3]

k = 6
print(solution.medianSlidingWindow(nums, k))

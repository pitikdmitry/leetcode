from heapq import heappush, heappop, _siftdown


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def balance(self):
        diff = len(self.max_heap) - len(self.min_heap)
        if diff == 2:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif diff == -2:
            heappush(self.max_heap, -heappop(self.min_heap))

    def insert(self, val: int):
        if len(self.max_heap) == 0 or val <= self.max_heap[0]:
            heappush(self.max_heap, -val)
        else:
            heappush(self.min_heap, val)
        self.balance()

    def delete(self, val: int):
        heap = self.min_heap
        if val <= -self.max_heap[0]:
            heap = self.max_heap
            val = -val

        idx = heap.index(val)
        heap[idx], heap[len(heap) - 1] = heap[len(heap) - 1], heap[idx]
        heap.pop()

        if idx < len(heap):
            _siftdown(heap, 0, idx)
        self.balance()

    def median(self):
        diff = len(self.max_heap) - len(self.min_heap)
        if diff == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif diff == 1:
            return -self.max_heap[0]
        return self.min_heap[0]

    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            self.insert(nums[i])

            if i >= k:
                self.delete(nums[i - k])

            if i >= k - 1:
                result.append(self.median())
        return result


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5, 8, 7, 6], 5)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()

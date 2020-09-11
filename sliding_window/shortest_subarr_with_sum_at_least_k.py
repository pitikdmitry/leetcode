'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:

Input: A = [2,-1,2], K = 3
Output: 3
'''
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, arr: List[int], K: int) -> int:
        pr_arr = [arr[i] for i in range(len(arr))]
        for i in range(1, len(arr)):
            pr_arr[i] = pr_arr[i - 1] + arr[i]

        #   increasing monotonic queue for pr_arr. Left value stores smallest prefix sum.
        #   pr[i] - d[0] determine sum inside sliding window
        d = deque()
        #   put zero prefix sum inside queue. val[0] - prefix sum value. val[1] - index
        d.append((0, -1))

        min_window_size = float('inf')
        #   sliding window on prefix array. right border of window - i.
        #   left border - smallest prefix sum from monotonic queue
        for i, val in enumerate(pr_arr):
            #   maintain increasing monotonic queue
            while len(d) > 0 and d[len(d) - 1][0] >= val:
                d.pop()

            d.append((val, i))

            #   window_sum = val - d[0][0]
            while len(d) > 0 and val - d[0][0] >= K:
                min_window_size = min(min_window_size, i - d[0][1])
                d.popleft()

        if min_window_size == float('inf'):
            return -1
        return min_window_size


solution = Solution()
# arr = [1, 8, 9, -3, 1, 26]
# arr = [8, 2, -3, 4]
arr = [2, 1, 3]
K = 3
print(solution.shortestSubarray(arr, K))

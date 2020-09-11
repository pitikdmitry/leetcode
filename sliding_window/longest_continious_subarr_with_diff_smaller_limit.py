'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty
subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
'''
from typing import List


#   We need to keep track of minimum and maximum value inside window
#   To do this we use increasing monotonic queue (min_dequeue) and decreasing monotonic queue (max_dequeue)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = []
        min_deque = []
        max_len = 0
        j = 0

        for i, num in enumerate(nums):
            #   maintain decreasing queue
            while len(max_deque) > 0 and max_deque[len(max_deque) - 1] < num:
                max_deque.pop(len(max_deque) - 1)

            #   maintain increasing queue
            while len(min_deque) > 0 and min_deque[len(min_deque) - 1] > num:
                min_deque.pop(len(min_deque) - 1)

            max_deque.append(num)
            min_deque.append(num)

            #   shrink window if diff of max and min value > limit
            while j < i and abs(max_deque[0] - min_deque[0]) > limit:
                if max_deque[0] == nums[j]:
                    max_deque.pop(0)
                if min_deque[0] == nums[j]:
                    min_deque.pop(0)

                j += 1

            max_len = max(max_len, i - j + 1)

        return max_len


solution = Solution()
nums = [8, 2, 4, 7]
limit = 4
print(solution.longestSubarray(nums, limit))

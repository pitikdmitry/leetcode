'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
from collections import deque
from typing import List


#   we use decreasing queue to store maximum values
#   queue[0] stores maximum value in current window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreasing_queue = deque()
        result = []
        for i, val in enumerate(nums):
            #   maintain queue
            while len(decreasing_queue) > 0 and val >= nums[decreasing_queue[-1]]:
                decreasing_queue.pop()

            #   remove values from previous windows
            if len(decreasing_queue) > 0 and decreasing_queue[0] <= i - k:
                decreasing_queue.popleft()

            decreasing_queue.append(i)
            if i >= k - 1:
                result.append(nums[decreasing_queue[0]])

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))

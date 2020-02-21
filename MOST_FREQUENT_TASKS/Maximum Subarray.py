'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        current_sum = float('-inf')
        max_sum = current_sum

        while j < len(nums):
            cur_element = nums[j]

            if cur_element >= current_sum + cur_element:
                i = j
                j += 1
                max_sum = max(max_sum, cur_element)
                current_sum = cur_element
            else:
                current_sum += cur_element
                max_sum = max(max_sum, current_sum)
                j += 1
        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))

'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the
left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot
indexes, you should return the left-most pivot index.
'''

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1

        left_sum = 0
        right_sum = sum(nums) - nums[0]

        for i in range(0, len(nums)):
            if left_sum == right_sum:
                return i

            if i == len(nums) - 1:
                return -1

            left_sum += nums[i]
            right_sum -= nums[i + 1]

        return -1


s = Solution()
nums = [1, 2, 3]
print(s.pivotIndex(nums))

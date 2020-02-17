'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        elif len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            prev_i = m - 1
            if prev_i == -1:
                prev_i = len(nums) - 1

            next_i = m + 1
            if next_i >= len(nums):
                next_i = 0

            if nums[m] < nums[prev_i] and nums[m] < nums[next_i]:
                return nums[m]

            elif nums[r] < nums[m]:
                #   go right
                l = m + 1
            else:
                r = m - 1

        return -1



s = Solution()
nums = [1, 2]
print(s.findMin(nums))

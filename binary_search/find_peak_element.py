'''A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.'''
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))

        l = 1
        r = len(nums) - 2

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m - 1

            if nums[m] > nums[m - 1]:
                l = m + 1
            else:
                r = m - 1

        return -1


s = Solution()
nums = [1]
print(s.findPeakElement(nums))

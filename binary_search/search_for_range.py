'''
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''
from typing import List


class Solution:
    def b_s(self, nums, target, left):
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                if left is True:
                    if m == 0:
                        return m
                    elif nums[m - 1] < nums[m]:
                        return m
                    else:
                        r = m - 1
                else:
                    if m == len(nums) - 1:
                        return m
                    elif nums[m + 1] > nums[m]:
                        return m
                    else:
                        l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.b_s(nums, target, True)
        r = self.b_s(nums, target, False)
        return [l, r]


nums = [5, 7, 7, 8, 8, 10]
target = 8

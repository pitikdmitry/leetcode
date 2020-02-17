'''
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''
from typing import List


class Solution:
    def find_right_border(self, nums, target, left, right):

    def binary_search_recursive(self, nums, target, left, right):
        if len(nums) == 0:
            return -1

        right_border = -1
        left_border = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                #   right border
                if m == len(nums) - 1:
                    right_border = m
                else:
                    if nums[m + 1] > nums[m]:
                        right_border = m
                    else:
                        right_border = self.binary_search_recursive(nums, target, m + 1, len(nums) - 1)

                if m == 0:
                    left_border = m
                else:
                    if nums[m - 1] < nums[m]:
                        left_border = m
                    else:
                        left_border = self.find_left_border(nums, target, 0, m - 1)


            elif nums[m] < target:
                r = m + 1
            else:
                l = m - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1
        return self.binary_search_recursive(nums, target, l, r)


nums = [5, 7, 7, 8, 8, 10]
target = 8

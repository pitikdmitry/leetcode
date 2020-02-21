'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                continue

            second = first + 1
            third = len(nums) - 1

            needed_el = -nums[first]
            while second < third:
                if second - first > 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue

                element = nums[second] + nums[third]
                if element == needed_el:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1

                elif element < needed_el:
                    second += 1
                else:
                    third -= 1

        return result


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))

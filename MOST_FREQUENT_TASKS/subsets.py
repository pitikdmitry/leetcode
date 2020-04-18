'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
from typing import List
from copy import deepcopy


class Solution:
    def helper(self, nums: List[int], start: int, end: int, cur_nums: List[int], result: List[List[int]]) -> None:
        result.append(deepcopy(cur_nums))

        for i in range(start, end + 1):
            cur_nums.append(nums[i])
            self.helper(nums, i + 1, end, cur_nums, result)
            cur_nums.pop(len(cur_nums) - 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, len(nums) - 1, [], result)
        return result


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))

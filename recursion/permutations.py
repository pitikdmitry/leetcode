

import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0, [], [])

    def helper(self, nums: List[int], start: int, arr: List[int], res: List[List[int]]) -> List[List[int]]:
        if len(arr) == len(nums):
            r = copy.deepcopy(arr)
            res.append(r)
            return res

        for i in range(start, len(nums)):
            arr.append(nums[i])
            res = self.helper(nums, start + 1, arr, res)
            arr.pop()

        return res


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))

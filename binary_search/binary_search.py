'''
Given a sorted (in ascending order) integer numsay nums of n elements and a target value,
write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int(((l - r) / 2) + r)
            cur = nums[m]
            if target == cur:
                return m
            elif target < cur:
                r = m - 1
            else:
                l = m + 1

        return -1


s = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(s.search(nums, target))

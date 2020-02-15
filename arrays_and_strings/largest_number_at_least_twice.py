'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
'''

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_el = max(nums)
        max_el_idx = nums.index(max_el)

        for idx, el in enumerate(nums):
            if max_el >= 2 * el or idx == max_el_idx:
                continue
            else:
                return -1

        return max_el_idx


s = Solution()
nums = [3, 6, 1, 0]
print(s.dominantIndex(nums))

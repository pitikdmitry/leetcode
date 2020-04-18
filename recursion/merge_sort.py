'''
Given an array of integers nums, sort the array in ascending order.
'''
from typing import List


class Solution:
    def merge(self, arr_1: List[int], arr_2: List[int]) -> List[int]:
        i, j = 0, 0
        res = []
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] <= arr_2[j]:
                res.append(arr_1[i])
                i += 1
            else:
                res.append(arr_2[j])
                j += 1

        while i < len(arr_1):
            res.append(arr_1[i])
            i += 1
        while j < len(arr_2):
            res.append(arr_2[j])
            j += 1
        return res

    def merge_sort(self, nums: List[int], i: int, j: int) -> List[int]:
        m = (i + j) // 2
        if i < j:
            res_1 = self.merge_sort(nums, i, m)
            res_2 = self.merge_sort(nums, m + 1, j)
            res = self.merge(res_1, res_2)
            return res
        return [nums[i]]

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums) - 1)


s = Solution()
nums = [5, 2, 3, 1]
sorted_nums = s.sortArray(nums)
print(sorted_nums)

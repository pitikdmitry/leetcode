'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always preferred.
'''
from typing import List


class Solution:
    def b_s(self, nums: List[int], target: int) -> tuple:
        if len(nums) == 0:
            return -1, -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m, m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l, r

    def get_closest(self, val_1: int, val_2: int, target: int) -> int:
        dif_1 = abs(val_1 - target)
        dif_2 = abs(val_2 - target)
        if dif_1 <= dif_2:
            return val_1
        return val_2

    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        if len(nums) == 0:
            return []

        m_1, m_2 = self.b_s(nums, x)

        m = self.get_closest(m_1, m_2, x)
        if m < 0:
            m = 0
        elif m >= len(nums):
            m = len(nums) - 1

        result = [nums[m]]

        i = m - 1
        j = m + 1
        amount = 1
        while i >= 0 and j < len(nums) and amount < k:
            closest = self.get_closest(nums[i], nums[j], x)
            if closest == nums[i]:
                result.insert(0, nums[i])
                i -= 1
            else:
                result.append(nums[j])
                j += 1
            amount += 1

        while i >= 0 and amount < k:
            result.insert(0, nums[i])
            i -= 1
            amount += 1

        while j < len(nums) and amount < k:
            result.append(nums[j])
            j += 1
            amount += 1
        return result


s = Solution()
nums = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
k = 3
x = 5
print(s.findClosestElements(nums, k, x))

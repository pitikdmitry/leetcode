'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''
from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if len(arr) == 0:
            return -1

        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return m

            if arr[l] <= arr[m]:
                if target <= arr[m] and target >= arr[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= arr[m] and target <= arr[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(s.search(nums, target))

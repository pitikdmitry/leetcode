'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
from typing import List


class Solution:
    def partition(self, arr, start, end):
        pivot = start
        l = start + 1
        r = end
        while l <= r:
            if arr[l] >= arr[pivot] and arr[r] < arr[pivot]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            elif arr[l] < arr[pivot]:
                l += 1
            else:
                r -= 1
        arr[r], arr[pivot] = arr[pivot], arr[r]
        return r

    def helper(self, arr, k, start, end):
        if start > end or start < 0 or end >= len(arr):
            return -1

        pos = self.partition(arr, start, end)
        end_pos = len(arr) - pos
        if end_pos == k:
            return arr[pos]
        elif end_pos > k:
            return self.helper(arr, k, pos + 1, end)
        else:
            return self.helper(arr, k, start, pos - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k, 0, len(nums) - 1)


s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums, k))

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
from typing import List


class Solution:
    def sort_array(self, arr, from_i, to_i):
        for i in range(from_i, to_i + 1):
            for j in range(i + 1, to_i + 1):
                if arr[i] >= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        swap_done = False
        cur = len(nums) - 1
        prev = cur - 1
        while prev >= 0:
            if nums[prev] < nums[cur] :
                #   find which to change
                smallest_diff = float('inf')
                index_to_change = cur
                for i in range(cur, len(nums)):
                    cur_diff = nums[i] - nums[prev]
                    if cur_diff < smallest_diff and cur_diff > 0 and nums[i] != 0:
                        smallest_diff = cur_diff
                        index_to_change = i

                nums[prev], nums[index_to_change] = nums[index_to_change], nums[prev]

                self.sort_array(nums, cur, len(nums) - 1)
                swap_done = True
                break
            else:
                prev -= 1
                cur -= 1

        if swap_done is False:
            nums.sort()


s = Solution()
nums = [2,2,4,0,1,2,4,4,0]
s.nextPermutation(nums)
print(nums)
#   solved with small error

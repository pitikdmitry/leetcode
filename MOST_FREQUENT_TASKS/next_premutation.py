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
    def reverse_nums(self, nums: List[int], start_i: int) -> None:
        i = start_i
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

    def nextPermutation(self, nums: List[int]) -> None:
        next_i = len(nums) - 1
        prev_i = next_i - 1
        while prev_i >= 0 and nums[prev_i] >= nums[next_i]:
            prev_i -= 1
            next_i -= 1

        if prev_i < 0:
            self.reverse_nums(nums, 0)
            return

        #   find next bigger
        prev_value = nums[prev_i]
        bigger_value = nums[next_i]
        bigger_value_i = next_i
        next_i += 1
        while next_i < len(nums):
            if prev_value < nums[next_i] <= bigger_value:
                bigger_value = nums[next_i]
                bigger_value_i = next_i

            next_i += 1

        #   swap next bigger and prev value
        nums[prev_i], nums[bigger_value_i] = nums[bigger_value_i], nums[prev_i]
        #   reverse right part
        self.reverse_nums(nums, prev_i + 1)
        return


s = Solution()
nums = [2, 2, 4, 0, 1, 2, 4, 4, 0]
s.nextPermutation(nums)
print(nums)

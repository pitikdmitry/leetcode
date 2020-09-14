'''
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        runner = 0
        while runner <= right:
            if nums[runner] == 1:
                runner += 1
            elif nums[runner] == 0:
                nums[left], nums[runner] = nums[runner], nums[left]
                left += 1
                runner += 1
            else:
                nums[runner], nums[right] = nums[right], nums[runner]
                right -= 1


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)

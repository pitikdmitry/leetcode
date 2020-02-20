'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
'''
from typing import List


class Solution:

    def trap(self, heights: List[int]) -> int:
        amount = 0
        left_level, right_level = 0, 0
        left = 0
        right = len(heights) - 1

        while left <= right:
            left_level = max(left_level, heights[left])
            right_level = max(right_level, heights[right])

            if right_level >= left_level:
                if left_level > heights[left]:
                    amount += left_level - heights[left]

                left += 1
            else:
                if right_level > heights[right]:
                    amount += right_level - heights[right]

                right -= 1

        return amount


s = Solution()
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(heights))

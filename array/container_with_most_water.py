'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_square = 0
        while i < j:

            cur_square = min(height[i], height[j]) * (j - i)
            max_square = max(max_square, cur_square)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_square


s = Solution()
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(heights))

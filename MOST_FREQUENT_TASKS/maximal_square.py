'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        dp = []
        for i in range(len(matrix)):
            cur = []
            for j in range(len(matrix[i])):
                el = 0 if matrix[i][j] == '0' else 1
                cur.append(el)
            dp.append(cur)

        max_square = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    up, left, up_left = 0, 0, 0
                    if i > 0:
                        up = dp[i - 1][j]
                    if j > 0:
                        left = dp[i][j - 1]
                    if i > 0 and j > 0:
                        up_left = dp[i - 1][j - 1]
                    dp[i][j] = min(up, left, up_left) + 1
                    max_square = max(max_square, dp[i][j])
        return max_square * max_square


s = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(s.maximalSquare(matrix))


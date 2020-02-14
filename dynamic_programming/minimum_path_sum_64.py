'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
from typing import List


class Solution:
    MAX_INT = float('inf')

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        memo = [[self.MAX_INT for j in range(m)] for i in range(n)]

        memo[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                s_1 = self.MAX_INT
                if i != 0:
                    s_1 = memo[i - 1][j]

                s_2 = self.MAX_INT
                if j != 0:
                    s_2 = memo[i][j - 1]

                memo[i][j] = min(s_1, s_2) + grid[i][j]

        return int(memo[n - 1][m - 1])


s = Solution()
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print(s.minPathSum(grid))

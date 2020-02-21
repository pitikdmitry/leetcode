'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
from queue import Queue
from typing import List


class Solution:
    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        q = Queue()
        q.put((i, j))

        while not q.empty():
            i, j = q.get()
            #   check i j
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                continue

            val = grid[i][j]
            if val == '1':
                grid[i][j] = '0'
                q.put((i + 1, j))
                q.put((i - 1, j))
                q.put((i, j + 1))
                q.put((i, j - 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        amount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    amount += 1
                    self.bfs(grid, i, j)

        return amount


s = Solution()
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(s.numIslands(grid))

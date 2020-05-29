'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
'''
from typing import List


class Solution:
    EMPTY_CELL = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2

    def get_neighbours(self, i: int, j: int) -> tuple:
        return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)

    def count_fresh_oranges(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.FRESH_ORANGE:
                    counter += 1
        return counter

    #   process via bfs
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.ROTTEN_ORANGE:
                    for new_i, new_j in self.get_neighbours(i, j):
                        q.append((new_i, new_j))

        steps = 0
        fresh_oranges = self.count_fresh_oranges(grid)
        #   do bfs, all neighbour oranges become rotten too
        while len(q) > 0:
            for i in range(len(q)):
                i, j = q.pop(0)

                if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                    continue

                if grid[i][j] != self.FRESH_ORANGE:
                    continue

                grid[i][j] = self.ROTTEN_ORANGE
                fresh_oranges -= 1
                for new_i, new_j in self.get_neighbours(i, j):
                    q.append((new_i, new_j))
            steps += 1

        #   if not all fresh oranges become rotten
        if fresh_oranges > 0:
            return -1
        #   if no steps required
        if steps == 0:
            return 0

        return steps - 1


solution = Solution()
grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]
print(solution.orangesRotting(grid))

'''
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1)
is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.
'''
from typing import List


class Solution:
    def get_neighbours(self, i: int, j: int) -> tuple:
        return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)

    #   bfs solution
    def maxDistance(self, matrix: List[List[int]]) -> int:
        q = []

        #   put in queue lands neighbours
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    for new_i, new_j in self.get_neighbours(i, j):
                        q.append((new_i, new_j))

        steps = 0
        has_water = False
        #   do bfs, process only water cells where distance is not already set
        while len(q) > 0:
            for i in range(len(q)):
                i, j = q.pop(0)
                if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                    continue

                if matrix[i][j] != 0:
                    continue

                has_water = True
                matrix[i][j] = steps + 1

                for new_i, new_j in self.get_neighbours(i, j):
                    q.append((new_i, new_j))

            steps += 1

        if has_water is True:
            return steps - 1
        return -1


solution = Solution()
matrix = [[1, 0, 1],
          [0, 0, 0],
          [1, 0, 1]]
print(solution.maxDistance(matrix))

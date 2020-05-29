'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
'''
from typing import List


#   BFS solution
class Solution:
    def get_neighbours(self, i: int, j: int) -> tuple:
        return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j, 0))

        visited = set()
        while len(q) > 0:
            i, j, val = q.pop(0)
            if (i, j) in visited:
                continue

            visited.add((i, j))
            matrix[i][j] = val

            for new_i, new_j in self.get_neighbours(i, j):
                if new_i < 0 or new_j < 0 or new_i >= len(matrix) or new_j >= len(matrix[0]):
                    continue

                q.append((new_i, new_j, val + 1))

        return matrix


solution = Solution()
matrix = [[1, 0, 0],
          [1, 1, 1],
          [1, 1, 1]]
print(solution.updateMatrix(matrix))

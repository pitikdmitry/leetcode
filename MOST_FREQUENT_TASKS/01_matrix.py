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

    def change_all_values(self, matrix, old_value, new_value):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == old_value:
                    matrix[i][j] = new_value

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        self.change_all_values(matrix, 1, -1)

        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for new_i, new_j in self.get_neighbours(i, j):
                        q.append((new_i, new_j))

        steps = 0
        while len(q) > 0:
            for i in range(len(q)):
                i, j = q.pop(0)

                if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                    continue

                if matrix[i][j] != -1:
                    continue

                matrix[i][j] = steps + 1

                for new_i, new_j in self.get_neighbours(i, j):
                    q.append((new_i, new_j))

            steps += 1
        return matrix


solution = Solution()
matrix = [[1, 0, 0],
          [1, 1, 1],
          [1, 1, 1]]
print(solution.updateMatrix(matrix))

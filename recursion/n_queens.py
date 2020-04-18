'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''
from typing import List


class Solution:
    def __init__(self) -> None:
        self.arr = []
        self.n = 0

    def remove_queen(self, row: int, col: int) -> None:
        self.arr[row][col] = False

    def add_queen(self, row: int, col: int) -> None:
        self.arr[row][col] = True

    def interfere(self, row: int, col: int) -> bool:
        for j in range(self.n):
            if self.arr[row][j] is True:
                return True

        for i in range(self.n):
            if self.arr[i][col] is True:
                return True

        i, j = row, col
        while i < self.n and j < self.n:
            if self.arr[i][j] is True:
                return True
            i += 1
            j += 1

        i, j = row, col
        while i >= 0 and j >= 0:
            if self.arr[i][j] is True:
                return True
            i -= 1
            j -= 1

        i, j = row, col
        while i < self.n and j >= 0:
            if self.arr[i][j] is True:
                return True
            i += 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < self.n:
            if self.arr[i][j] is True:
                return True
            i -= 1
            j += 1

        return False

    def queens(self, row: int, count: int, res: List[int]) -> int:
        for col in range(self.n):
            if not self.interfere(row, col):
                self.add_queen(row, col)
                count += 1
                if row == self.n - 1 and count == self.n:
                    res[0] += 1
                else:
                    count = self.queens(row + 1, count, res)

                self.remove_queen(row, col)
                count -= 1

        return count

    def totalNQueens(self, n: int) -> int:
        self.n = n
        res = [0]
        self.arr = [[False for j in range(n)] for i in range(n)]
        self.queens(0, 0, res)
        return res[0]


s = Solution()
print(s.totalNQueens(5))

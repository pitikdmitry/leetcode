'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
from typing import List


class Solution:
    def get_directions(self, i: int, j: int) -> tuple:
        return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)

    #   dfs has special bool parameter. If it true -> we paint visited islands
    def dfs(self, board: List[List[str]], visited: set, i: int, j: int, paint: bool) -> None:
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'X':
            return

        if (i, j) in visited:
            return
        visited.add((i, j))

        if paint is True:
            board[i][j] = 'X'

        for new_i, new_j in self.get_directions(i, j):
            self.dfs(board, visited, new_i, new_j, paint)

    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return

        #   go by all boundaries if find O -> start DFS from here and add all island to visited,
        #   because it is bad island
        visited = set()
        #   upper boundary
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.dfs(board, visited, 0, j, False)

        #   bottom boundary
        last_row_i = len(board) - 1
        for j in range(len(board[last_row_i])):
            if board[last_row_i][j] == 'O':
                self.dfs(board, visited, last_row_i, j, False)

        #   left boundary
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, visited, i, 0, False)

        #   right boundary
        last_col_i = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][last_col_i] == 'O':
                self.dfs(board, visited, i, last_col_i, False)

        #   go through inner part and paint all good islands
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] == 'O':
                    self.dfs(board, visited, i, j, True)


solution = Solution()
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ]
solution.solve(board)
print(board)

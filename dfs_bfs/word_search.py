'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
from typing import List


class Solution:
    def backtrack(self, board, i, j, visited, s, str_i):
        if str_i == len(s):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != s[str_i]:
            return False

        if (i, j) in visited:
            return False

        visited.add((i, j))
        res = self.backtrack(board, i + 1, j, visited, s, str_i + 1) or \
              self.backtrack(board, i - 1, j, visited, s, str_i + 1) or \
              self.backtrack(board, i, j + 1, visited, s, str_i + 1) or \
              self.backtrack(board, i, j - 1, visited, s, str_i + 1)

        visited.remove((i, j))
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True

        if len(board) == 0:
            return False

        first_letter = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_letter:
                    res = self.backtrack(board, i, j, set(), word, 0)
                    if res is True:
                        return res
        return False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'ABCCED'

print(s.exist(board, word))

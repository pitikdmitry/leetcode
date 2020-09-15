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
from typing import List, Tuple, Set


class Solution:
    #   we use visited set to prevent cycles (every letter can be used one time)
    def dfs(self, board: List[List[str]], i: int, j: int, s: str, str_i: int, visited: Set[Tuple[int, int]]) -> bool:

        if str_i == len(s):
            return True

        if (i, j) in visited:
            return False
        visited.add((i, j))

        #   check border
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != s[str_i]:
            return False

        return self.dfs(board, i + 1, j, s, str_i + 1, visited) or \
               self.dfs(board, i - 1, j, s, str_i + 1, visited) or \
               self.dfs(board, i, j + 1, s, str_i + 1, visited) or \
               self.dfs(board, i, j - 1, s, str_i + 1, visited)

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True

        #   start dfs from every letter and try to find word
        first_letter = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_letter:
                    res = self.dfs(board, i, j, word, 0, set())
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

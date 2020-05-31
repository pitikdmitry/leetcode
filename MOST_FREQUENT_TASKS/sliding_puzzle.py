'''
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
'''

import itertools
from typing import List, Tuple
from copy import deepcopy


class Solution:
    #   find zero element
    def find_zero(self, board: List[List[int]]) -> Tuple[int, int]:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    return i, j
        return -1, -1

    #   convert 2D array to a hashable object
    def get_hash(self, board: List[List[int]]) -> Tuple[int, int]:
        expended_list = list(itertools.chain(*board))
        return tuple(expended_list)

    #   we can move zero element to 4 directions
    def get_neighbour_indexes(self, i: int, j: int) -> List[Tuple[int, int]]:
        return [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]

    #   checking if indexes are out of range
    def check_idx(self, board: List[List[int]], i: int, j: int) -> bool:
        if i < 0 or i >= len(board):
            return False
        if j < 0 or j >= len(board[0]):
            return False

        return True

    #   simple BFS
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        steps = 0
        expected_answer = (1, 2, 3, 4, 5, 0)
        q = []
        q.append(board)
        visited = set()

        while len(q) > 0:
            for k in range(len(q)):
                board = q.pop(0)
                key = self.get_hash(board)

                if key == expected_answer:
                    return steps

                if key in visited:
                    continue

                visited.add(key)
                i, j = self.find_zero(board)
                indexes = self.get_neighbour_indexes(i, j)
                for new_i, new_j in indexes:
                    if self.check_idx(board, new_i, new_j) is False:
                        continue

                    board_copy = deepcopy(board)
                    board_copy[i][j], board_copy[new_i][new_j] = board_copy[new_i][new_j], board_copy[i][j]
                    q.append(board_copy)
            steps += 1

        return -1


solution = Solution()
board = [[4, 1, 2],
         [5, 0, 3]]
print(solution.slidingPuzzle(board))

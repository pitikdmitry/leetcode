'''
Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #   in every dp element we keep three values 0 - maximum vertical length of ones.
        #   1 - max horizontal length of ones
        #   2 - max square
        dp = [[[0, 0, 0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        VERTIVAL_LEN_POS, HORIZONTAL_LEN_POS, MAX_SQUARE_POS = 0, 1, 2
        max_el = 0

        for i in range(0, len(dp)):
            for j in range(0, len(dp[0])):
                if matrix[i][j] == '0':
                    continue

                dp[i][j] = [1, 1, 1]

                if i == 0 and j == 0:
                    continue

                if i > 0:
                    dp[i][j][VERTIVAL_LEN_POS] = dp[i - 1][j][VERTIVAL_LEN_POS] + 1

                if j > 0:
                    dp[i][j][HORIZONTAL_LEN_POS] = dp[i][j - 1][HORIZONTAL_LEN_POS] + 1

                #   we try to find shorter row of ones in upper rows
                min_row_width = dp[i][j][HORIZONTAL_LEN_POS]
                for upper_row_diff in range(1, dp[i][j][VERTIVAL_LEN_POS]):
                    current_row_idx = i - upper_row_diff
                    current_row_width = dp[current_row_idx][j][HORIZONTAL_LEN_POS]
                    min_row_width = min(min_row_width, current_row_width)

                #   we try to find shorter column of ones in upper columns
                min_column_length = dp[i][j][VERTIVAL_LEN_POS]
                for left_col_dif in range(1, dp[i][j][HORIZONTAL_LEN_POS]):
                    current_col_idx = j - left_col_dif
                    current_col_length = dp[current_col_idx][j][VERTIVAL_LEN_POS]
                    min_column_length = min(min_column_length, current_col_length)

                square = min_row_width * min_column_length
                dp[i][j][MAX_SQUARE_POS] = max(dp[i][j][VERTIVAL_LEN_POS], dp[i][j][HORIZONTAL_LEN_POS], square)

                max_el = max(max_el, dp[i][j][MAX_SQUARE_POS])

        return max_el


solution = Solution()
matrix=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(solution.maximalRectangle(matrix))
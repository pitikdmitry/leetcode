'''
Given a positive integer n, find the least number of perfect
 square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import math
from typing import List, Dict


#   we have given number n. We generate list square nums and try to subtract every perfect square from n
#   next we process remaining part of n (n - square_nums[i])
class SolutionTopDown:
    def squares_recursive(self, n: int, memo: Dict[int, int], square_nums: List[int]):
        if n == 0:
            return 0

        if n < 0:
            return float('inf')

        if n in memo:
            return memo[n]

        min_res = float('inf')
        #   we try to subtract every perfect square
        for i in square_nums:
            res = self.squares_recursive(n - i, memo, square_nums)
            min_res = min(min_res, res + 1)

        memo[n] = min_res
        return min_res

    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)), 0, -1)]
        res = self.squares_recursive(n, {}, square_nums)
        if res == float('inf'):
            return -1
        return res


s = SolutionTopDown()
print(s.numSquares(13))


class SolutionBottomUp:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n) + 1))]
        dp = [float('inf') for _ in range(0, n + 1)]
        for el in square_nums:
            dp[el] = 1

        for i in range(2, len(dp)):
            for el in square_nums:
                if el >= i:
                    break
                dp[i] = min(dp[i], dp[i - el] + 1)

        return dp[len(dp) - 1]


s = SolutionBottomUp()
print(s.numSquares(13))

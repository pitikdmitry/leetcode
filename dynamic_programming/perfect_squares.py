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


class Solution2:
    def is_perfect_square(self, num):
        num_sqrt = int(math.sqrt(num))
        if num_sqrt * num_sqrt == num:
            return True

        return False

    def helper(self, n, memo):
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)), 0, -1)]

        if n == 0:
            return 0

        if n < 0:
            return float('inf')

        if n in memo:
            return memo[n]

        min_res = float('inf')
        for i in square_nums:
            if self.is_perfect_square(i) is True:
                res = self.helper(n - i, memo)
                min_res = min(min_res, res + 1)

        memo[n] = min_res
        return min_res

    def numSquares(self, n: int) -> int:
        return self.helper(n, dict())


s = Solution2()
print(s.numSquares(12))


class Solution:
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


s = Solution()
print(s.numSquares(13))

'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
'''
from typing import List, Dict


#   top down with memoization
#   every time try to take every kind of coin
class Solution:
    def helper(self, coins: List[int], amount: int, memo: Dict):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1

        if amount in memo:
            return memo[amount]

        min_res = float('inf')
        for coin in coins:
            res = self.helper(coins, amount - coin, memo)
            if res != -1:
                min_res = min(min_res, res + 1)

        memo[amount] = min_res
        return min_res

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.helper(coins, amount, {})
        if res == float('inf'):
            return -1
        return res


#   bottom up
class SolutionBottomUp:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for j in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(dp)):
            dp[i][0] = 0

        for i in range(len(dp)):
            for j in range(1, len(dp[0])):
                c1 = float('inf')
                new_j = j - coins[i]
                if new_j >= 0:
                    c1 = dp[i][new_j] + 1

                c2 = float('inf')
                if i > 0:
                    c2 = dp[i - 1][j]

                dp[i][j] = min(c1, c2)
        res = dp[len(dp) - 1][len(dp[0]) - 1]
        if res == float('inf'):
            return -1
        return res


solution = Solution()
solution_bottom_up = SolutionBottomUp()
coins = [2, 5, 10, 1]
amount = 27
print(solution.coinChange(coins, amount))
print(solution_bottom_up.coinChange(coins, amount))

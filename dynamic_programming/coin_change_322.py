'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
'''
from typing import List, Dict


class Solution:
    def helper(self, coins: List[int], remaining: int, memo: Dict):
        if remaining == 0:
            return 0
        elif remaining < 0:
            return -1

        if remaining in memo:
            return memo[remaining]

        min_res = float('inf')
        for coin in coins:
            res = self.helper(coins, remaining - coin, memo)
            if 0 <= res < min_res:
                min_res = min(min_res, res) + 1

        if min_res == float('inf'):
            memo[remaining] = -1
        else:
            memo[remaining] = min_res
        return memo[remaining]

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        return self.helper(coins, amount, {})


s = Solution()
coins = [186, 419, 83, 408]
amount = 6249
print(s.coinChange(coins, amount))

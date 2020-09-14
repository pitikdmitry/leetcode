'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''


from typing import List, Dict, Tuple


#   recursive memo solution. Memo key -> coins start idx + amount of money left
#   unbounded knapsack pattern
class Solution:
    def helper(self, amount: int, coins: List[int], coin_idx: int, memo: Dict[Tuple[int, int], int]) -> int:
        if amount == 0:
            return 1

        if (amount, coin_idx) in memo:
            return memo[(amount, coin_idx)]

        results = []
        for i in range(coin_idx, len(coins)):
            if amount - coins[i] < 0:
                continue

            res = self.helper(amount - coins[i], coins, i, memo)
            results.append(res)

        memo[(amount, coin_idx)] = sum(results)
        return memo[(amount, coin_idx)]

    def change(self, amount: int, coins: List[int]) -> int:
        return self.helper(amount, coins, 0, {})


coins = [1, 2, 5]
amount = 5
solution = Solution()
print(solution.change(amount, coins))


#   DP bottom up solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        if len(coins) == 0:
            return 0

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        #   all values in first column = 1 because we have one way to get amount=0
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(len(dp)):
            for j in range(1, len(dp[0])):
                ways = 0
                #   number of ways without taking current item
                if i > 0:
                    ways += dp[i - 1][j]

                #   number of ways o=if we take current item
                new_j = j - coins[i]
                if new_j >= 0:
                    ways += dp[i][new_j]

                dp[i][j] = ways

        return dp[len(dp) - 1][len(dp[0]) - 1]


coins = [1, 2, 5]
amount = 5
solution = Solution()
print(solution.change(amount, coins))

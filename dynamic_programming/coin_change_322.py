'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
'''
from typing import List, Dict


#   top down
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


#   bottom up
class SolutionBottomUp:
    def coinChange(self, coins: List[int], target: int) -> int:
        if target == 0:
            return 0

        coins_amount = [float('inf') for _ in range(target + 1)]
        for coin in coins:
            if coin < len(coins_amount):
                coins_amount[coin] = 1

        for i in range(len(coins_amount)):
            # print(f'i: {i}, val: {coins_amount[i]}')
            if coins_amount[i] == float('inf'):
                continue

            if i == target:
                return int(coins_amount[i])
            else:
                for coin in coins:
                    new_idx = i + coin
                    new_val = coins_amount[i] + 1

                    if new_idx < len(coins_amount) and new_val < coins_amount[new_idx]:
                        coins_amount[new_idx] = new_val

        return -1


s = Solution()
solution_bottom_up = SolutionBottomUp()
coins = [186, 419, 83, 408]
coins = sorted(coins, reverse=True)
amount = 6249
print(s.coinChange(coins, amount))
print(solution_bottom_up.coinChange(coins, amount))

'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
'''
from typing import List, Dict


#   naive recursive solution with memoization
class Solution:
    #   count max profit for one transaction in one array
    def array_max_profit(self, prices: List[int], start: int, end: int, memo: Dict[tuple]) -> int:
        if len(prices) == 0:
            return 0

        if (start, end) in memo:
            return memo[(start, end)]

        current_min = prices[start]
        max_diff = 0
        for i in range(start, end + 1):
            cur_price = prices[i]
            current_min = min(cur_price, current_min)

            diff = prices[i] - current_min
            max_diff = max(diff, max_diff)

        memo[(start, end)] = max_diff
        return max_diff

    def helper(self, k: int, prices: List[int], start: int, end: int, memo: Dict[tuple]) -> int:
        if k == 0 or start >= end:
            return 0

        if (start, end, k) in memo:
            return memo[(start, end, k)]

        max_res = 0
        for current_end in range(start, end + 1):
            res = self.array_max_profit(prices, start, current_end, memo)
            res += self.helper(k - 1, prices, current_end + 1, end, memo)

            max_res = max(max_res, res)

        memo[(start, end, k)] = max_res
        return max_res

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.helper(k, prices, 0, len(prices) - 1, {})


s = Solution()
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
k = 2
print(s.maxProfit(k, prices))

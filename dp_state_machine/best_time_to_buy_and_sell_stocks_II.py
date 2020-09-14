'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peak, valley = 0, 0
        i = 1
        profit = 0

        while i < len(prices):

            #   finding valley
            while i < len(prices) and prices[i] < prices[i - 1]:
                valley = i
                i += 1

            #   finding peak
            while i < len(prices) and prices[i] >= prices[i - 1]:
                peak = i
                i += 1

            #   check if we have found peak after valley or array ended
            if peak > valley:
                profit += prices[peak] - prices[valley]

        return profit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))

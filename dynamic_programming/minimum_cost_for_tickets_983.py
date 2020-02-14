'''
In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.
Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
'''
from typing import List, Dict


class Solution:
    def helper(self, days: List[int], costs: List[int], cur_day: int, days_left: int, money_spent: int, memo: Dict):
        if cur_day == 366:
            return money_spent

        if cur_day in memo:
            return memo[cur_day]

        if days_left > 0:
            return self.helper(days, costs, cur_day + 1, days_left - 1, money_spent, memo)

        if days_left == 0 and cur_day not in days:
            return self.helper(days, costs, cur_day + 1, days_left, money_spent, memo)
        elif days_left == 0:
            res_1 = self.helper(days, costs, cur_day + 1, 0, money_spent + costs[0], memo)
            res_2 = self.helper(days, costs, cur_day + 1, 6, money_spent + costs[1], memo)
            res_3 = self.helper(days, costs, cur_day + 1, 29, money_spent + costs[2], memo)
            result = min(res_1, res_2, res_3)
            memo[cur_day] = result
            return memo[cur_day]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.helper(days, costs, 1, 0, 0, {})


s = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(s.mincostTickets(days, costs))

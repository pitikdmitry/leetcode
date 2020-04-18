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
    def helper(self, days: set, costs: List[int], cur_day: int, memo: Dict) -> int:
        if cur_day > 365:
            return 0

        if cur_day in memo:
            return memo[cur_day]

        if cur_day not in days:
            return self.helper(days, costs, cur_day + 1, memo)
        else:
            res_3 = self.helper(days, costs, cur_day + 30, memo)
            res_3 += costs[2]
            res_2 = self.helper(days, costs, cur_day + 7, memo)
            res_2 += costs[1]
            res_1 = self.helper(days, costs, cur_day + 1, memo)
            res_1 += costs[0]

            result = min(res_1, res_2, res_3)
            memo[cur_day] = result
            return memo[cur_day]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        return self.helper(days, costs, 1, {})


s = Solution()
days = [4, 5, 9, 11, 14, 16, 17, 19, 21, 22, 24]
costs = [1, 4, 18]
print(s.mincostTickets(days, costs))

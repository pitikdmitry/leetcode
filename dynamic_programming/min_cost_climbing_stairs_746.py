'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.
'''
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) == 1 or len(cost) == 2:
            return cost[0]

        val_first = cost[0]
        val_second = cost[1]

        for i in range(2, len(cost)):
            current_val = min(val_first, val_second) + cost[i]
            val_first = val_second
            val_second = current_val

        return min(val_first, val_second)


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))

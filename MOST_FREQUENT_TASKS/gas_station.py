'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
 You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3
'''


from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #   check if we can complete circuit
        gas_sum = sum(gas)
        cost_sum = sum(cost)
        if cost_sum > gas_sum:
            return -1

        #   find starting pos, if window_gas_amount < 0, we move start_index and try new window
        start_i, cur_i = 0, 0
        window_length, window_gas_amount = 0, 0

        while window_length < len(gas):
            if cur_i >= len(gas):
                cur_i = cur_i % len(gas)

            window_gas_amount += gas[cur_i] - cost[cur_i]
            if window_gas_amount >= 0:
                cur_i += 1
                window_length += 1
            else:
                start_i += 1
                cur_i = start_i
                window_length = 0
                window_gas_amount = 0

        return start_i


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(s.canCompleteCircuit(gas, cost))

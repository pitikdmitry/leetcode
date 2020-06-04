'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.
The goal is to get the maximum profit from the items in the knapsack.
The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit.
Here are the weights and profits of the fruits:

Items: { Apple, Orange, Melon }
Weights: { 1, 2, 3 }
Profits: { 15, 20, 50 }
Knapsack capacity: 5
'''
from typing import List, Dict


#   recursive memo solution. We call only items with bigger index. Because we don't want to recompute dublicates.
#   In this task it's not important, but in other questions with this pattern we may have wrong answer
def helper(weights: List[int], profits: List[int], capacity: int, memo: Dict[int, int]):
    if capacity <= 0:
        return 0

    if capacity in memo:
        return memo[capacity]

    results = []
    i = 0
    while i < len(weights):
        weight, profit = weights[i], profits[i]
        if capacity - weight < 0:
            i += 1
            continue

        res = helper(weights, profits, capacity - weight, memo)
        results.append(res + profit)

        i += 1

    result = 0
    if len(results) > 0:
        result = max(results)

    memo[capacity] = result
    return result


def unbounded_knapsack(weights: List[int], profits: List[int], capacity: int) -> int:
    return helper(weights, profits, capacity, {})


weights = [1, 3, 4, 5]
profits = [15, 50, 60, 90]
capacity = 6
print(unbounded_knapsack(weights, profits, capacity))


#   bottom up dp solution
def unbounded_knapsack_bottom_up(weights: List[int], profits: List[int], capacity: int) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights))]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            #   if we take current item
            take = 0
            new_j = j - weights[i]
            if new_j >= 0:
                take = dp[i][new_j] + profits[i]

            #   if we dont take current item -> we take result from the previous row
            not_take = 0
            if i > 0:
                not_take = dp[i - 1][j]

            #   choose better option
            dp[i][j] = max(take, not_take)

    return dp[len(dp) - 1][len(dp[0]) - 1]


weights = [1, 3, 4, 5]
profits = [15, 50, 60, 90]
capacity = 6
print(unbounded_knapsack_bottom_up(weights, profits, capacity))

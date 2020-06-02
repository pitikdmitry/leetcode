'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.
The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once,
as we don’t have multiple quantities of any item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit.
Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
'''
from typing import List, Dict


#   iterative bottom up solution with optimized space 1D array
def get_maximum_profit_bottom_up(weights: List[int], profits: List[int], capacity: int) -> int:
    if capacity == 0:
        return 0

    #   initialized DP 1D array
    dp = [0 for _ in range(capacity + 1)]
    #   setup DP
    for i in range(len(dp)):
        if i >= weights[0]:
            dp[i] = profits[0]

    #   do a cycle for every item in weights
    for i in range(1, len(weights)):
        #   count profit for every capacity value
        new_dp = [0 for _ in range(capacity + 1)]
        for j in range(0, len(dp)):
            #   we don't take current item
            without_item = dp[j]

            #   we take current item
            new_j = j - weights[i]
            with_item = 0
            if new_j >= 0:
                with_item = dp[new_j] + profits[i]

            #   choose better variant
            new_dp[j] = max(without_item, with_item)

        #   update dp array
        dp = new_dp

    return dp[len(dp) - 1]


#   Recursive + memo top down solution
def helper(weights: List[int], profits: List[int], capacity: int, cur_idx: int, memo: Dict[tuple, int]):
    if cur_idx == len(weights):
        return 0

    if (cur_idx, capacity) in memo:
        return memo[(cur_idx, capacity)]

    with_item = 0
    #   add this item to knapsack if we can do it
    if capacity - weights[cur_idx] >= 0:
        with_item = helper(weights, profits, capacity - weights[cur_idx], cur_idx + 1, memo) + profits[cur_idx]

    #   move forward without adding current item to knapsack
    without_item = helper(weights, profits, capacity, cur_idx + 1, memo)

    memo[(cur_idx, capacity)] = max(with_item, without_item)
    return memo[(cur_idx, capacity)]


def get_maximum_profit(weights: List[int], profits: List[int], capacity: int) -> int:
    return helper(weights, profits, capacity, 0, {})


weights = [2, 3, 1, 4]
profits = [4, 5, 3, 7]
capacity = 5
print(get_maximum_profit_bottom_up(weights, profits, capacity))
print(get_maximum_profit(weights, profits, capacity))

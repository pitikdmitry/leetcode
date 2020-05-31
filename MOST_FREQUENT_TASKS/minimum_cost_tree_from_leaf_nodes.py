'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
(Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.



Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
'''
from typing import List, Tuple, Dict


#   DP recursive + memo
class Solution:
    #   return (sum, max_left)
    #   memo key: (left, right), memo value: (min_sum, max_leaf)
    def helper(self, nums: List[int], left: int, right: int, memo: Dict[Tuple[int, int], Tuple[int, int]]):
        if right < left:
            return 0, 0

        if right == left:
            return 0, nums[left]

        if (left, right) in memo:
            return memo[(left, right)]

        min_sum = float('inf')
        max_leaf = 0
        for center in range(left, right):
            left_sum, left_max_leaf = self.helper(nums, left, center, memo)
            right_sum, right_max_leaf = self.helper(nums, center + 1, right, memo)
            result = left_sum + right_sum + (left_max_leaf * right_max_leaf)

            if result < min_sum:
                min_sum = result
                max_leaf = max(left_max_leaf, right_max_leaf)

        memo[(left, right)] = (min_sum, max_leaf)
        return min_sum, max_leaf

    def mctFromLeafValues(self, nums: List[int]) -> int:
        min_sum, _ = self.helper(nums, 0, len(nums) - 1, {})
        return min_sum


solution = Solution()
nums = [6, 2, 4]
print(solution.mctFromLeafValues(nums))

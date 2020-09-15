'''Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   '''
from typing import Dict


#   top down solution with memoization
#   in given range from start to end we choose every value as root of subtree
#   and then we process left and right subtrees
#   for every root we need to multiply amount of left and right subtrees
#   (because we can have various combinations of trees)
class Solution:
    def helper(self, start: int, end: int, memo: Dict):
        if (start, end) in memo:
            return memo[(start, end)]
        if end - start == 1:
            return 2
        if end - start < 1:
            return 1

        count = 0
        for center in range(start, end + 1):
            #   left subtree
            start_l = start
            end_l = center - 1

            #   right subtree
            start_r = center + 1
            end_r = end

            c1 = self.helper(start_l, end_l, memo)
            c2 = self.helper(start_r, end_r, memo)
            count += c1 * c2
        memo[(start, end)] = count
        return count

    def numTrees(self, n: int) -> int:
        return self.helper(1, n, {})


s = Solution()
print(s.numTrees(4))

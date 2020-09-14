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


class Solution:
    def helper(self, start: int, end: int, memo: Dict):
        if (start, end) in memo:
            return memo[(start, end)]
        if end - start == 1:
            return 2
        if end - start < 1:
            return 1

        count = 0
        for i in range(start, end + 1):
            start_l = start
            end_l = i - 1

            start_r = i + 1
            end_r = end

            res_1 = self.helper(start_l, end_l, memo)
            res_2 = self.helper(start_r, end_r, memo)
            count += res_1 * res_2
        memo[(start, end)] = count
        return count

    def numTrees(self, n: int) -> int:
        return self.helper(1, n, {})


s = Solution()
print(s.numTrees(4))

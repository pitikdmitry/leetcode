'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


from typing import List
import copy


class Solution:
    def helper(self, cur: List[int], result: List[List[int]], n: int, k: int, i: int) -> None:
        if len(cur) == k:
            res = copy.deepcopy(cur)
            result.append(res)
            return

        while i <= n:
            cur.append(i)
            i += 1
            self.helper(cur, result, n, k, i)
            cur.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.helper([], result, n, k, 1)
        return result


s = Solution()
n = 4
k = 2
print(s.combine(n, k))

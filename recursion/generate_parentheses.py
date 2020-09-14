'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
from typing import List


class Solution:
    def gen_helper(self, n: int, current_str: str, left: int, right: int, result: List[str]) -> None:
        if len(current_str) == 2 * n:
            result.append(current_str)
            return

        if left < n:
            self.gen_helper(n, current_str + '(', left + 1, right, result)

        if right < left:
            self.gen_helper(n, current_str + ')', left, right + 1, result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.gen_helper(n, '', 0, 0, result)
        return result


s = Solution()
print(s.generateParenthesis(3))

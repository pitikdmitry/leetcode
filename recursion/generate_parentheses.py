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
    def gen_helper(self, n: int, current_str: str, result: List[str]):
        if len(current_str) == n:
            result.append(current_str)
            return

        for i in range(n):
            current_str += '('
            self.gen_helper(n, current_str, result)
            current_str = current_str[:-1]

            current_str += ')'
            self.gen_helper(n, current_str, result)
            current_str = current_str[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.gen_helper(n, '', result)
        return result


s = Solution()
print(s.generateParenthesis(2))

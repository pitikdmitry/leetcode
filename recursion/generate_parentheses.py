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
    def check_balance(self, current_str: str) -> bool:
        stack = []
        for c in current_str:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False

                prev = stack.pop()
                if prev != '(':
                    return False

        if len(stack) != 0:
            return False
        return True

    def gen_helper(self, n: int, current_str: str, result: set):
        if len(current_str) == 2 * n:
            if self.check_balance(current_str) is True:
                result.add(current_str)
            return

        for i in range(n):
            current_str += '('
            self.gen_helper(n, current_str, result)
            current_str = current_str[:-1]

            current_str += ')'
            self.gen_helper(n, current_str, result)
            current_str = current_str[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        self.gen_helper(n, '', result)
        return list(result)


s = Solution()
print(s.generateParenthesis(3))

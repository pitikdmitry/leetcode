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


class SolutionSlow:
    def check_balance(self, current_str: str) -> bool:
        balance = 0
        for c in current_str:
            if c == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return balance == 0

    def gen_helper(self, n: int, start_i: int, current_str: str, result: []) -> None:
        if len(current_str) == 2 * n:
            if self.check_balance(current_str) is True:
                result.append(current_str)
            return

        for i in range(start_i, 2 * n):
            current_str += '('
            self.gen_helper(n, i + 1, current_str, result)
            current_str = current_str[:-1]

            current_str += ')'
            self.gen_helper(n, i + 1, current_str, result)
            current_str = current_str[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.gen_helper(n, 0, '', result)
        return result


s = SolutionSlow()
print(s.generateParenthesis(3))

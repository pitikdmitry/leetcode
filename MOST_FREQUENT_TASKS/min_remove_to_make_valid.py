'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bad_idxs = set()
        stack = []
        for idx, el in enumerate(s):
            if el == '(':
                stack.append(idx)
            elif el == ')':
                if len(stack) == 0:
                    bad_idxs.add(idx)
                else:
                    stack.pop()

        for idx in stack:
            bad_idxs.add(idx)

        new_s = ''
        for i in range(len(s)):
            if i not in bad_idxs:
                new_s += s[i]

        return new_s


solution = Solution()
s = 'lee(t(c)o)de)'
print(solution.minRemoveToMakeValid(s))

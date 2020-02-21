'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                last_bracket = stack.pop()
                if c == ')' and last_bracket != '(':
                    return False
                elif c == '}' and last_bracket != '{':
                    return False
                elif c == ']' and last_bracket != '[':
                    return False

        if len(stack) != 0:
            return False
        return True

'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                current_s = ''
                while stack[len(stack) - 1] != '[':
                    letter = stack.pop(len(stack) - 1)
                    current_s = letter + current_s

                stack.pop(len(stack) - 1)
                number = ''
                while len(stack) > 0 and stack[len(stack) - 1].isdigit() is True:
                    number = stack.pop(len(stack) - 1) + number
                number = int(number)
                current_s *= number
                stack.append(current_s)
            else:
                stack.append(c)

        result_s = ''
        while len(stack) > 0:
            letter = stack.pop(len(stack) - 1)
            result_s = letter + result_s
        return result_s


solution = Solution()
# s = '2[abc]3[cd]ef'
s = '100[leet]'
print(solution.decodeString(s))

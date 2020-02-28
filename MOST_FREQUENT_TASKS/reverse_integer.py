'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''


class Solution:
    def reverse_str(self, s) -> str:
        s_list = []
        for c in s:
            s_list.append(c)
        i = 0
        j = len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ''.join(s_list)

    def check_integer_range(self, num: int) -> bool:
        if num > (2 ** 31) - 1 or num < -(2 ** 31):
            return False
        return True

    def reverse(self, x: int) -> int:
        if not self.check_integer_range(x):
            return 0

        s = str(x)
        if len(s) == 0:
            return x
        if s[0] == '-':
            s = '-' + self.reverse_str(s[1:])
        else:
            s = self.reverse_str(s)

        num = int(s)
        if not self.check_integer_range(num):
            return 0

        return num


s = Solution()
print(s.reverse(-123))

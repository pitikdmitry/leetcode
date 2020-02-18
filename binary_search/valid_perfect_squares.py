'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            m = (l + r) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 < num:
                l = m + 1
            else:
                r = m - 1
        return False


s = Solution()
print(s.isPerfectSquare(14))

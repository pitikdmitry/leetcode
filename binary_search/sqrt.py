'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''


class Solution:
    def mySqrt(self, target: int) -> int:
        if target == 0:
            return 0
        if target == 1:
            return 1

        l = 0
        r = target

        while l <= r:
            m = int(((l - r) / 2) + r)
            cur = m ** 2
            if target == cur:
                return m
            elif target < cur:
                r = m - 1
            else:
                l = m + 1

        if l ** 2 > target:
            return l - 1
        else:
            return l


s = Solution()
target = 145
print(s.mySqrt(target))

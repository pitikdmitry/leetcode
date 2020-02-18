'''Implement pow(x, n), which calculates x raised to the power n (xn).'''


class Solution:
    def helper(self, x: float, n: int, memo: dict) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x

        if n in memo:
            return memo[n]

        if n < 0:
            return 1 / self.helper(x, abs(n), memo)

        if n % 2 == 0:
            half_pow = self.helper(x, n // 2, memo)
            memo[n] = half_pow * half_pow
        else:
            half_pow = self.helper(x, n // 2, memo)
            memo[n] = half_pow * half_pow * x

        return memo[n]

    def myPow(self, x: float, n: int) -> float:
        return self.helper(x, n, {})


s = Solution()
x = 2.00000
n = 10
print(s.myPow(x, n))

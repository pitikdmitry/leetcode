'''
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
That is, F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
'''


class Solution:
    def cache_dec(func):
        memo = {}

        def wrapper(*args, **kwargs):
            n = args[len(args) - 1]
            if n in memo:
                return memo[n]

            res = func(*args, **kwargs)
            print(f'n: {n}, res: {res}')

            memo[n] = res
            return res
        return wrapper

    @cache_dec
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


s = Solution()
print(s.fib(10))

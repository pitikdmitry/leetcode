'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''


class Solution:
    def helper(self, n: int, i: int) -> int:
        if i == n:
            return 1
        elif i > n:
            return 0

        return self.helper(n, i + 1) + self.helper(n, i + 2)

    def climbStairs(self, n: int) -> int:
        return self.helper(n, 0)


s = Solution()
print(s.climbStairs(10))

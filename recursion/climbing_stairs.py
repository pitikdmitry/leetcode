'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''


class Solution:
    def helper(self, n, i, res):
        if i == n:
            res[0] += 1
        elif i > n:
            return

        self.helper(n, i + 1, res)
        self.helper(n, i + 2, res)

    def climbStairs(self, n: int) -> int:
        res = [0]
        self.helper(n, 0, res)
        return res[0]


s = Solution()
print(s.climbStairs(10))

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


#   can be optimized with memo
class SolutionRecursive:
    def is_valid(self, s: str) -> bool:
        if len(s) > 2 or int(s) > 26 or int(s) < 1:
            return False
        return True

    def helper(self, s: str, start: int) -> None:
        if start == len(s):
            self.result += 1
            return

        cur_s = ''
        for i in range(start, start + 2):
            if i >= len(s):
                return

            cur_s += s[i]

            if self.is_valid(cur_s):
                self.helper(s, i + 1)

            cur_s = cur_s[:-1]

    def numDecodings(self, s: str) -> int:
        self.result = 0
        self.helper(s, 0)
        return self.result


solution = SolutionRecursive()
s = "226"
print(solution.numDecodings(s))


# DP bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(dp) - 1]


solution = Solution()
s = "0"
print(solution.numDecodings(s))

'''
Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
'''
from typing import Dict, Tuple


#   we have two pointers one on start of the string, second on end
#   if s[start] == s[end] we increase length of subsequence and process remaining part of string
#   if not we try to move one of the pointers
class Solution:
    def helper(self, s: str, start: int, end: int, memo: Dict[Tuple[int, int], int]) -> int:
        if start == end:
            return 1
        if start > end:
            return 0

        if (start, end) in memo:
            return memo[(start, end)]

        result = 0
        if s[start] == s[end]:
            result = self.helper(s, start + 1, end - 1, memo) + 2
        else:
            c1 = self.helper(s, start + 1, end, memo)
            c2 = self.helper(s, start, end - 1, memo)
            result = max(c1, c2)

        memo[(start, end)] = result
        return result

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s, 0, len(s) - 1, {})


solution = Solution()
s = 'bbbab'
print(solution.longestPalindromeSubseq(s))


#   DP solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == j:
                    dp[i][j] = 1

        for i in range(len(dp) - 2, -1, -1):
            for j in range(i + 1, len(dp[i])):

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[0][len(dp[0]) - 1]


solution_bottom_up = Solution()
s = 'bbbab'
print(solution_bottom_up.longestPalindromeSubseq(s))

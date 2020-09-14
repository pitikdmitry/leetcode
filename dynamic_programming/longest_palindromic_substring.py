'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
from typing import Tuple


#   recursive memo solution
#   returns tuple with longest substring length and longest substring
class Solution:
    def helper(self, s: str, start: int, end: int) -> Tuple[int, str]:
        if start > end:
            return 0, ''
        if start == end:
            return 1, s[start]

        results = []
        if s[start] == s[end]:
            estimated_result = end - start - 1
            length, longest_substr = self.helper(s, start + 1, end - 1)
            #   we need to check if shorter substring is palindrome
            if length == estimated_result:
                length += 2
                longest_substr = s[start: end + 1]

            results.append((length, longest_substr))

        length, substr = self.helper(s, start + 1, end)
        results.append((length, substr))
        length, substr = self.helper(s, start, end - 1)
        results.append((length, substr))

        r = max(results, key=lambda x: x[0])
        return r

    def longestPalindrome(self, s: str) -> str:
        length, substr = self.helper(s, 0, len(s) - 1)
        return substr


solution = Solution()
s = 'abddbca'
print(solution.longestPalindrome(s))


#   DP solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(dp)):
            for j in range(len(dp)):
                if i == j:
                    dp[i][j] = True

        max_length = 0
        max_palindrome = s[0]
        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[0]) - 1, i, -1):
                #   str from i...j is palindrome if str without first two symbols is palindrome or
                #   if length of str == 2 and symbols are equals
                if (s[i] == s[j] and dp[i + 1][j - 1] is True) or (s[i] == s[j] and j - i + 1 == 2):
                    dp[i][j] = True
                    length = j - i + 1
                    if length >= max_length:
                        max_length = length
                        max_palindrome = s[i: j + 1]
        return max_palindrome


solution = Solution()
s = 'abddbca'
print(solution.longestPalindrome(s))

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
            result = self.helper(s, start + 1, end, memo)
            result = max(result, self.helper(s, start, end - 1, memo))

        memo[(start, end)] = result
        return result

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s, 0, len(s) - 1, {})


solution = Solution()
s = 'bbbab'
print(solution.longestPalindromeSubseq(s))

'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
'''
from typing import Dict, Tuple


#   longest common
class Solution:
    def longest_common_subsequence_recursive(self, text1: str, text2: str, i1: int, i2: int, memo: Dict[Tuple[int, int], int]) -> int:
        if i1 == len(text1) or i2 == len(text2):
            return 0

        if (i1, i2) in memo:
            return memo[(i1, i2)]

        if text1[i1] == text2[i2]:
            res = self.longest_common_subsequence_recursive(text1, text2, i1 + 1, i2 + 1, memo) + 1
            return res

        res_1 = self.longest_common_subsequence_recursive(text1, text2, i1, i2 + 1, memo)
        res_2 = self.longest_common_subsequence_recursive(text1, text2, i1 + 1, i2, memo)
        memo[(i1, i2)] = max(res_1, res_2)
        return memo[(i1, i2)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longest_common_subsequence_recursive(text1, text2, 0, 0, {})


solution = Solution()
text1 = "abcde"
text2 = "ace"
print(solution.longestCommonSubsequence(text1, text2))

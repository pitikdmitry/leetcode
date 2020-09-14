'''
Given two strings s_1, s_2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s_1 = "sea", s_2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
'''


class Solution:
    def minimumDeleteSum(self, s_1: str, s_2: str) -> int:
        #   insert empty symbol for more comfortable indexation
        s_1 = ' ' + s_1
        s_2 = ' ' + s_2

        #   create DP table
        dp = [[0 for _ in range(len(s_1))] for _ in range(len(s_2))]

        #   fill first row with ascii sum of symbols from s_1[1...j]
        for j in range(1, len(dp[0])):
            dp[0][j] = ord(s_1[j]) + dp[0][j - 1]

        #   fill first column with ascii sum of symbols from s_2[1...i]
        for i in range(1, len(dp)):
            dp[i][0] = ord(s_2[i]) + dp[i - 1][0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s_1[j] == s_2[i]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s_2[i]), dp[i][j - 1] + ord(s_1[j]))

        return dp[len(dp) - 1][len(dp[0]) - 1]


solution = Solution()
s_1 = 'delete'
s_2 = 'leet'
print(solution.minimumDeleteSum(s_1, s_2))

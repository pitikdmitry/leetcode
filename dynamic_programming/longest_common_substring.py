'''
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
'''
from typing import Dict, Tuple


#   if we have same characters in s1[i1] and s2[i2] we don't necessary need to take it to longest substr.
#   We try to take and to skip character and when recursion comes back we choose best variant
def find_LCS_length_recursive(s1: str, s2: str, i1: int, i2: int, amount: int, memo: Dict[Tuple[int, int, int], int]) -> int:
    if i1 == len(s1) or i2 == len(s2):
        return amount

    if (i1, i2, amount) in memo:
        return memo[(i1, i2, amount)]

    results = [amount]
    if s1[i1] == s2[i2]:
        res = find_LCS_length_recursive(s1, s2, i1 + 1, i2 + 1, amount + 1, memo)
        results.append(res)

    res = find_LCS_length_recursive(s1, s2, i1 + 1, i2, 0, memo)
    results.append(res)
    res = find_LCS_length_recursive(s1, s2, i1, i2 + 1, 0, memo)
    results.append(res)

    memo[(i1, i2, amount)] = max(results)
    return memo[(i1, i2, amount)]


def find_LCS_length(s1, s2) -> int:
    memo = {}
    r = find_LCS_length_recursive(s1, s2, 0, 0, 0, memo)
    return r


print(find_LCS_length("abdca", "cbda"))
print(find_LCS_length("passport", "ppsspt"))


def find_LCS_length_bottom_up(s1: str, s2: str) -> int:
    #   dp table is one element bigger, we use it for not checking borders
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    max_length = 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            #   offset as dp table is one element bigger
            s1_char = s1[i - 1]
            s2_char = s2[j - 1]
            if s1_char == s2_char:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    return max_length


print(find_LCS_length_bottom_up("abdca", "cbda"))
print(find_LCS_length_bottom_up("passport", "ppsspt"))

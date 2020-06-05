'''
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
'''
from typing import Dict, Tuple


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
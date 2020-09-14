'''
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.
'''

#   In other words we need to find smallest window which has all symbols from extra_symbols dictionary

from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        #   count all letters
        freq = Counter()
        for c in s:
            freq[c] += 1

        #   count frequences of extra symbols, needed in window
        extra_symbols = {}
        for key, value in freq.items():
            value -= len(s) // 4
            if value > 0:
                extra_symbols[key] = value

        match = len(extra_symbols)
        if match == 0:
            return 0

        min_size = len(s)
        j = 0
        for i, c in enumerate(s):
            if c not in extra_symbols:
                continue

            extra_symbols[c] -= 1
            if extra_symbols[c] == 0:
                match -= 1

            #   shrink sliding window
            while j <= i and match == 0:
                if s[j] not in extra_symbols:
                    j += 1
                    continue

                min_size = min(min_size, i - j + 1)
                extra_symbols[s[j]] += 1
                if extra_symbols[s[j]] == 1:
                    match += 1
                j += 1

        return min_size


solution = Solution()
s = 'QQWEWQRQ'
print(solution.balancedString(s))

'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''
from collections import Counter


#   sliding window approach with hashmap
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        letters_amount, max_len, j = 0, 0, 0

        for i in range(len(s)):
            counter[s[i]] += 1
            if counter[s[i]] == 1:
                letters_amount += 1

            if letters_amount <= k:
                max_len = max(max_len, i - j + 1)

            while letters_amount > k and j < i:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    letters_amount -= 1
                j += 1

        return max_len


solution = Solution()
s = 'eceba'
k = 2
print(solution.lengthOfLongestSubstringKDistinct(s, k))

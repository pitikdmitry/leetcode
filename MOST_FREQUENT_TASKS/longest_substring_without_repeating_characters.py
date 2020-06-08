'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        bad_letters, max_length, j = 0, 0, 0
        for i in range(len(s)):
            counter[s[i]] += 1

            if counter[s[i]] == 2:
                bad_letters += 1

            while bad_letters > 0:
                counter[s[j]] -= 1
                if counter[s[j]] == 1:
                    bad_letters -= 1

                j += 1

            max_length = max(max_length, i - j + 1)

        return max_length


solution = Solution()
s = 'pwwkew'
print(solution.lengthOfLongestSubstring(s))

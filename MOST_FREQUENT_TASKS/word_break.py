'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''
from typing import List


class Solution:
    def helper(self, s, words, memo):
        if len(s) == 0:
            return True
        if s in memo:
            return memo[s]

        for i in range(len(s)):
            cur_word = s[0: i + 1]
            if cur_word in words:
                word_remains = s[i + 1:]
                res = self.helper(word_remains, words, memo)
                memo[word_remains] = res

                if res is True:
                    return True

        return False

    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        words = set(wordList)
        return self.helper(s, words, {})


solution = Solution()
s = 'applepenapple'
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))


class SolutionBottomUp:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        words = set(wordList)
        found_word = [False for x in range(len(s))]
        if len(words) == 0:
            return False

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if j == 0 or found_word[j - 1] is True:
                    cur_word = s[j: i + 1]
                    if cur_word in words:
                        found_word[i] = True

        return found_word[len(found_word) - 1]


solution = SolutionBottomUp()
s = 'applepenapple'
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))

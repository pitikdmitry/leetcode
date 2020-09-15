'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

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
from typing import List, Set


#   from every index in s we try to match every word from word dict,
#   if find match -> process ramaining part of string
class Solution:
    def word_break_recursive(self, s: str, str_i: int, words: Set[str], memo):
        if str_i == len(s):
            return True
        if str_i in memo:
            return memo[str_i]

        res = False
        for word in words:
            #   try to read word from s of length = len(word)
            next_word_in_str = s[str_i: str_i + len(word)]
            if next_word_in_str == word:
                res |= self.word_break_recursive(s, str_i + len(word), words, memo)

        memo[str_i] = res
        return res

    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        words = set(wordList)
        return self.word_break_recursive(s, 0, words, {})


solution = Solution()
s = 'applepenapple'
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))


class SolutionBottomUp:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        words = set(wordList)
        #   dp[i] indicates if we can reach this index with given word list
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(dp)):
            for word in words:
                word_length = len(word)

                if i - word_length < 0 or dp[i - word_length] == False:
                    continue

                #   compare word from wordList and word from s, which ends on i - 1 index
                word_from_str = s[i - word_length: i]
                if word_from_str == word:
                    dp[i] = True
                    break

        return dp[len(dp) - 1]


solution = SolutionBottomUp()
s = 'applepenapple'
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))

'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only
if we can add exactly one letter anywhere in word1 to make it equal to word2.
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

'''
from typing import List


class Solution2:
    def is_descessor(self, word1, word2):
        counter = {}
        for c in word2:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for c in word1:
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            else:
                return False

        if len(counter) != 1:
            return False

        for key, value in counter.items():
            if value != 1:
                return False

        return True

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0

        words = sorted(words, key=len)

        max_chain_lengths = []
        for i in range(len(words)):
            cur_chain_length = 1
            for j in range(i - 1, -1, -1):
                if len(words[i]) - len(words[j]) == 0:
                    continue
                elif len(words[i]) - len(words[j]) > 1:
                    break
                if self.is_descessor(words[j], words[i]) is True:
                    cur_chain_length = max(max_chain_lengths[j] + 1, cur_chain_length)

            max_chain_lengths.append(cur_chain_length)

        return max(max_chain_lengths)


s = Solution2()
words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(s.longestStrChain(words))


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        d = {}
        for word in words:
            for i in range(len(word)):
                #   we delete one symbol and search this word in dict
                word_to_search = word[:i] + word[i + 1:]
                child_length = d.get(word_to_search, 0)
                if word not in d:
                    d[word] = child_length + 1
                else:
                    d[word] = max(child_length + 1, d[word])

        max_value = 0
        for val in d.values():
            max_value = max(max_value, val)
        return max_value


s = Solution()
words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(s.longestStrChain(words))

'''
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.
'''


from collections import defaultdict


#   In other words we need longest substring where bad_characters = window_size - frequency[most_frequent_char]
#   and bad_characters <= k. We will maintain biggest_frequency_of_char after every shrink of window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fr = defaultdict(int)
        j = 0
        max_len, biggest_frequency_of_char = 0, 0

        for i, ch in enumerate(s):
            fr[ch] += 1
            biggest_frequency_of_char = max(biggest_frequency_of_char, fr[ch])

            bad_characters_in_window = (i - j + 1) - biggest_frequency_of_char
            while j < i and bad_characters_in_window > k:
                fr[s[j]] -= 1
                j += 1
                #   update most frequent character (biggest_frequency_of_char)
                for c, ch_frequency in fr.items():
                    biggest_frequency_of_char = max(biggest_frequency_of_char, ch_frequency)
                    bad_characters_in_window = (i - j + 1) - biggest_frequency_of_char

            max_len = max(max_len, i - j + 1)

        return max_len


solution = Solution()
s = "AABABBA"
k = 1
print(solution.characterReplacement(s, k))

'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters
 and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''
from typing import List


class Solution:
    def count_length(self, words: List[str]) -> int:
        length = 0
        for word in words:
            length += len(word)

        return length

    def insert_spaces_in_one_word_line(self, text: str, max_width: int) -> str:
        needed_spaces = max_width - len(text)
        return text + ' ' * needed_spaces

    def create_spaces_list(self, words_list: List[str], max_width: int) -> List[str]:
        words_length = self.count_length(words_list)

        all_spaces_amount = max_width - words_length
        spaces_intervals_amount = len(words_list) - 1
        spaces_in_every_interval = all_spaces_amount // spaces_intervals_amount
        additional_spaces = all_spaces_amount - spaces_in_every_interval * spaces_intervals_amount

        spaces_list = []
        for i in range(spaces_intervals_amount):
            spaces_list.append(' ' * spaces_in_every_interval)

        space_interval_idx = 0
        while additional_spaces > 0:
            spaces_list[space_interval_idx] += ' '
            additional_spaces -= 1
            space_interval_idx += 1

        return spaces_list

    def insert_spaces(self, words: List[str], max_width) -> List[str]:
        row_i = 0
        words_with_spaces_list = []

        #   we don't process last row here
        while row_i < len(words):
            #   process last row by another rule
            if row_i == len(words) - 1:
                last_row = self.insert_spaces_in_one_word_line(words[row_i], max_width)
                words_with_spaces_list.append(last_row)
                break

            words_list = words[row_i].split()
            row_with_spaces = ''
            #   processing string with one word has another rule
            if len(words_list) == 1:
                row_with_spaces = self.insert_spaces_in_one_word_line(words[row_i], max_width)

            #   processing string with many words
            elif len(words_list) > 1:
                spaces_list = self.create_spaces_list(words_list, max_width)

                #   merge words and spaces list
                i, j = 0, 0
                while i < len(words_list) and j < len(spaces_list):
                    row_with_spaces += words_list[i] + spaces_list[j]
                    i += 1
                    j += 1

                #   append last word
                if i < len(words_list):
                    row_with_spaces += words_list[i]
                    i += 1

            words_with_spaces_list.append(row_with_spaces)
            row_i += 1

        return words_with_spaces_list

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        result_words = []
        cur_str = ''

        #   fill words in result array with only one space
        word_idx = 0
        while word_idx < len(words):
            cur_word = words[word_idx]
            if len(cur_str) == 0:
                cur_str = words[word_idx]
            else:
                if len(cur_str) + 1 + len(cur_word) <= max_width:
                    cur_str += ' ' + cur_word
                else:
                    result_words.append(cur_str)
                    cur_str = ''
                    continue
            word_idx += 1

        if len(cur_str) > 0:
            result_words.append(cur_str)

        result_words = self.insert_spaces(result_words, max_width)
        return result_words


solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
print(solution.fullJustify(words, max_width))

'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
'''
from typing import List


class Solution:
    def helper(self, letters: List[str], array_number: int, cur_word: str, result: List[str]):
        if array_number == len(letters):
            result.append(cur_word)
            return

        arr = letters[array_number]

        for i in range(len(arr)):
            cur_word += arr[i]
            self.helper(letters, array_number + 1, cur_word, result)
            cur_word = cur_word[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        letters = []
        for digit in digits:
            letters.append(d[int(digit)])
        result = []
        if len(letters) == 0:
            return result

        self.helper(letters, 0, '', result)
        return result


s = Solution()
digits = '258'
print(s.letterCombinations(digits))

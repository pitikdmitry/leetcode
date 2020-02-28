'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.
'''
from functools import cmp_to_key
from typing import List


class Solution:
    def is_digit_log(self, log: str) -> bool:
        i = 0
        while i < len(log):
            if log[i] == ' ':
                i += 1
                break
            i += 1

        if i == len(log):
            return False
        if log[i].isdigit():
            return True
        return False

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_res = []
        letter_res = []
        for log in logs:
            is_digit = self.is_digit_log(log)
            if is_digit is True:
                digit_res.append(log)
            else:
                letter_res.append(log)

        def comparator(x, y):
            splitted_x = x.split(' ')
            x_key = splitted_x.pop(0)
            x = ' '.join(splitted_x)

            splitted_y = y.split(' ')
            y_key = splitted_y.pop(0)
            y = ' '.join(splitted_y)

            i, j = 0, 0
            while i < len(x) and j < len(y):
                if ord(x[i]) < ord(y[j]):
                    return -1
                elif ord(x[i]) > ord(y[j]):
                    return 1
                else:
                    i += 1
                    j += 1

            if i == len(x) and j == len(y):
                if x_key < y_key:
                    return -1
                else:
                    return 1
            elif i < len(x):
                return -1
            else:
                return 1

        letter_res = sorted(letter_res, key=cmp_to_key(comparator))
        letter_res.extend(digit_res)
        return letter_res


s = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(s.reorderLogFiles(logs))

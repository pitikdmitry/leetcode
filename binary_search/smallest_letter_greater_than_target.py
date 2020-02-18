'''
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
'''
from typing import List


class Solution:
    def b_s_right_target(self, letters: List[str], target: str) -> int:
        target = ord(target)
        if len(letters) == 0:
            return -1

        l = 0
        r = len(letters) - 1

        while l <= r:
            m = int(((l - r) / 2) + r)
            cur = ord(letters[m])
            if target == cur:
                if m == len(letters) - 1:
                    return m + 1
                else:
                    next = ord(letters[m + 1])
                    if cur == next:
                        l = m + 1
                    else:
                        return m + 1
            elif target < cur:
                r = m - 1
            else:
                l = m + 1

        return l

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        greatest_letter_idx = self.b_s_right_target(letters, target)
        if greatest_letter_idx == len(letters):
            greatest_letter_idx = 0
        return letters[greatest_letter_idx]


s = Solution()
letters = ["c", "f", "j"]
target = "g"
print(s.nextGreatestLetter(letters, target))

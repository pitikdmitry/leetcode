'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

'''
from typing import List


class Solution:
    def reverse_helper(self, s: List[str], i: int) -> None:
        if i == len(s) // 2:
            return

        j = len(s) - 1 - i
        s[i], s[j] = s[j], s[i]
        self.reverse_helper(s, i + 1)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_helper(s, 0)


s = Solution()
text = ['a', 'b', 'c', 'd']
s.reverseString(text)
print(text)

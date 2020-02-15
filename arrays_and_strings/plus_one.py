'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
from typing import List


class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        carry = 1
        for i in range(len(arr) - 1, -1, -1):
            arr[i] += carry
            if arr[i] > 9:
                carry = 1
                arr[i] -= 10
            else:
                carry = 0

        if carry == 1:
            arr = [1] + arr

        return arr


s = Solution()
digits = [4, 3, 2, 1]
print(s.plusOne(digits))

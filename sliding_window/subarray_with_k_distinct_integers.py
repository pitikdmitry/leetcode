'''
Given an array A of positive integers, call a (contiguous, not necessarily distinct)
subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
'''

from collections import Counter
from typing import List


#   To find number of subarrays with exactly K distinct integers
#   we will count subarrays with at most K distinct integers and at most (K - 1) distinct integers
class Solution:
    def subarray_at_most_K(self, arr: List[int], K: int) -> int:
        fr = Counter()

        j, match = 0, 0
        subarrays_amount = 0
        for i in range(len(arr)):
            fr[arr[i]] += 1
            if fr[arr[i]] == 1:
                match += 1

            while match > K:
                fr[arr[j]] -= 1
                if fr[arr[j]] == 0:
                    match -= 1
                j += 1

            #   add subarrays even if amount of integers in window < K
            subarrays_amount += i - j + 1

        return subarrays_amount

    def subarraysWithKDistinct(self, arr: List[int], K: int) -> int:
        return self.subarray_at_most_K(arr, K) - self.subarray_at_most_K(arr, K - 1)


solution = Solution()
A = [1, 2, 1, 2, 3]
K = 2
print(solution.subarraysWithKDistinct(A, K))

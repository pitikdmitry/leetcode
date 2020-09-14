'''
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a
(contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
'''
from typing import List


#   we maintain queue where we store end indexes of flips
#   if amount of elements is odd -> it means that we don't need to flip zero value
#   number of elements in queue determine how many times we have flipped this element
class Solution:
    def minKBitFlips(self, arr: List[int], K: int) -> int:
        q = []
        flips = 0
        #   i indicates left border of window
        for i in range(len(arr)):
            while len(q) > 0 and q[0] < i:
                q.pop(0)

            #   need flip current index
            if (arr[i] == 0 and len(q) % 2 == 0) or (arr[i] == 1 and len(q) % 2 != 0):
                last_index_in_flip = i + K - 1  # right border of window
                if last_index_in_flip >= len(arr):  # unable to do K bit flip
                    return -1

                flips += 1
                q.append(last_index_in_flip)

        return flips


solution = Solution()
arr = [0, 0, 0, 1, 0, 1, 1, 0]
K = 3
print(solution.minKBitFlips(arr, K))

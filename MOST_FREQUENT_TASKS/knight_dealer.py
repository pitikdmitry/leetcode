'''
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.
Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight),
it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10
'''
from typing import Dict


#   recursive memoized solution
class Solution:
    def get_neighbors(self, current_number: int):
        neighbors = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [6, 2],
            8: [3, 1],
            9: [2, 4],
            0: [6, 4]
        }
        return neighbors[current_number]

    def helper(self, N: int, current_button: int, memo: Dict):
        if N == 0:
            return 1

        #   N represents how many clicks we need to do
        if (N, current_button) in memo:
            return memo[(N, current_button)]

        res = 0
        #   do recursive call for all neighbours
        for neighbor in self.get_neighbors(current_button):
            res += self.helper(N - 1, neighbor, memo)

        memo[(N, current_button)] = res
        return memo[(N, current_button)]

    def knightDialer(self, N: int) -> int:
        res = 0
        memo = {}
        for i in range(0, 10):
            res += self.helper(N - 1, i, memo)

        return res % (10 ** 9 + 7)


solution = Solution()
print(solution.knightDialer(1))

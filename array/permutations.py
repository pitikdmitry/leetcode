'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from typing import List


#   BFS approach. we add num by num to every position in previous permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        #   take num
        for num in nums:

            new_permutations = []
            #   take every old permutations and add num to every position
            for perm in permutations:
                for idx_to_insert in range(0, len(perm) + 1):
                    new_perm = list(perm)
                    new_perm.insert(idx_to_insert, num)
                    new_permutations.append(new_perm)

            permutations = new_permutations

        return permutations


solution = Solution()
nums = [1, 2, 3]
print(solution.permute(nums))

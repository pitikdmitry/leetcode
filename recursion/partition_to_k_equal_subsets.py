'''
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''


from typing import List


#   recursive backtracking solution
class Solution:
    def helper(self, nums: List[int], used: List[int], used_amount: int, target: int, cur_s: int, k: int) -> bool:
        if cur_s == target:
            #   found answer
            if k == 1 and used_amount == len(nums):
                return True
            #   found answer, but not all elements are used
            elif k == 1:
                return False
            #   found not all subsets
            else:
                return self.helper(nums, used, used_amount, target, 0, k - 1)
        elif cur_s > target:
            return False

        i = 0
        #   try to take every unused number
        while i < len(nums):
            if used[i] is True:
                i += 1
                continue

            used[i] = True
            res = self.helper(nums, used, used_amount + 1, target, cur_s + nums[i], k)
            used[i] = False

            if res is True:
                return True
            i += 1

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        used = [False for _ in range(len(nums))]
        return self.helper(nums, used, 0, target, 0, k)


solution = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(solution.canPartitionKSubsets(nums, k))

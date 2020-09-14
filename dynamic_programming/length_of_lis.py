'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
from typing import List, Dict


#   added memoization to recursion
class Solution:
    def helper(self, nums: List[int], idx: int, prev_idx: int, memo: Dict[int, int]) -> 0:
        if idx == len(nums):
            return 0

        if (idx, prev_idx) in memo:
            return memo[idx]

        c1 = 0
        #   take this value. We can take current value if and only if it is bigger than previous
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            #   we add this value to sequence, so we increase max value by one
            c1 = self.helper(nums, idx + 1, idx, memo) + 1

        #   don't take this value
        c2 = self.helper(nums, idx + 1, prev_idx, memo)
        memo[idx] = max(c1, c2)
        return memo[idx]

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(nums, 0, -1, {})


solution = Solution()
nums = [9, 2, 5, 3]
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums))


class SolutionBottomUp:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1 for i in range(len(nums))]
        max_lis = 1

        #   dp[i] = max LIS ending on index i
        for i in range(1, len(nums)):
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

                max_lis = max(max_lis, dp[i])

        return max_lis


solution_bottom_up = SolutionBottomUp()
nums = [9, 2, 5, 3]
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution_bottom_up.lengthOfLIS(nums))

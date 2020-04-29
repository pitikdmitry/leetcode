'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''
from typing import List


# dp bottom up solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target_sum = sum(nums) // 2

        #   insert dummy number for more comfortable indexation
        nums.insert(0, -1)

        dp = [[0 for i in range(0, int(target_sum + 1))] for j in range(len(nums))]

        #   i - means that we use items from [0, i] (items from nums)
        #   j - current sum value
        #   dp[i][j] - how many ways to achieve this sum
        #   arr[i - 1][j] - situation, when we don't add nums[i] item
        #   arr[i - 1][j - item_amount] - situation, when we add nums[i] item (we use it)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                item_amount = nums[i]
                previous_sum = j - item_amount
                if previous_sum < 0:
                    previous_sum = 0

                dp[i][j] = dp[i - 1][j] + dp[i - 1][previous_sum]
                if j == item_amount:
                    dp[i][j] += 1

        return dp[len(dp) - 1][len(dp[0]) - 1] != 0


solution = Solution()
nums = [1, 5, 11, 5]
print(solution.canPartition(nums))

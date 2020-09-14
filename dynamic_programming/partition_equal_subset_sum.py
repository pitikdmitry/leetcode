'''
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''
from typing import List, Dict, Tuple


#   We go through all values and do two recursive calls either we take it or not
#   we try to get their sum = sum(nums) // 2
class Solution:
    def can_partition_recursive(self, nums: List[int], idx: int, sum: int, memo: Dict[Tuple[int, int], bool]) -> bool:
        if sum == 0:
            return True
        elif idx == len(nums) or sum < 0:
            return False

        if (idx, sum) in memo:
            return memo[(idx, sum)]

        #   take
        c1 = self.can_partition_recursive(nums, idx + 1, sum - nums[idx], memo)
        #   not take
        c2 = self.can_partition_recursive(nums, idx + 1, sum, memo)
        memo[(idx, sum)] = c1 or c2
        return memo[(idx, sum)]

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target_sum = sum(nums) // 2
        return self.can_partition_recursive(nums, 0, target_sum, {})


solution = Solution()
nums = [1, 5, 11, 5]
print(solution.canPartition(nums))


# dp bottom up solution
class SolutionBottomUp:
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


solution_bottom_up = SolutionBottomUp()
nums = [1, 5, 11, 5]
print(solution.canPartition(nums))

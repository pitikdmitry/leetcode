from typing import List


class Solution:
    def helper(self, arr, target, cur_s, k):
        if cur_s == target:
            if k == 1 and len(arr) == 0:
                return True
            elif k == 1:
                return False
            else:
                return self.helper(arr, target, 0, k - 1)
        elif cur_s > target:
            return False

        i = 0
        while i < len(arr):
            val = arr.pop(i)
            res = self.helper(arr, target, cur_s + val, k)
            arr.insert(i, val)
            if res is True:
                return True
            i += 1

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = int(sum(nums) / k)
        return self.helper(nums, target, 0, k)


solution = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(solution.canPartitionKSubsets(nums, k))

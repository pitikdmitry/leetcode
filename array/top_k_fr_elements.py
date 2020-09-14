from collections import defaultdict
from typing import List


class Solution:
    def partition(self, nums, start, end, fr):
        pivot_i = start
        i = start + 1
        j = end
        while i <= j:
            while i < len(nums) and fr[nums[i]] >= fr[nums[pivot_i]]:
                i += 1
            while j > pivot_i and fr[nums[j]] < fr[nums[pivot_i]]:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        #   swap pivot and j
        nums[pivot_i], nums[j] = nums[j], nums[pivot_i]
        return j

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k -= 1
        fr = defaultdict(int)
        for num in nums:
            fr[num] += 1

        unique_nums = list(fr.keys())

        start = 0
        end = len(unique_nums) - 1
        while start < end:
            pos = self.partition(unique_nums, start, end, fr)
            if pos == k:
                return unique_nums[0:pos + 1]
            elif pos < k:
                start = pos + 1
            else:
                end = pos - 1

        return unique_nums[0:start + 1]


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))


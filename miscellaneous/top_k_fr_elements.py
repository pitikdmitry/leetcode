'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


from collections import defaultdict
from typing import List, Dict


#   Quickselect solution
class Solution:
    #   partition function find position for pivot element
    def partition(self, nums: List[int], start: int, end: int, fr: Dict[int, int]):
        pivot_i = start
        i, j = start + 1, end
        while i <= j:
            #   finding element < pivot
            while i < len(nums) and fr[nums[i]] >= fr[nums[pivot_i]]:
                i += 1

            #   finding element >= pivot
            while j > pivot_i and fr[nums[j]] < fr[nums[pivot_i]]:
                j -= 1

            #   swap
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        #   swap pivot and j
        nums[pivot_i], nums[j] = nums[j], nums[pivot_i]
        return j

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k -= 1
        #   count frequency of every element
        fr = defaultdict(int)
        for num in nums:
            fr[num] += 1

        unique_nums = list(fr.keys())

        start, end = 0, len(unique_nums) - 1
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


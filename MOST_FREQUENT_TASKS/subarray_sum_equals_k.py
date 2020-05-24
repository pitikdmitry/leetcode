'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
from collections import defaultdict
from typing import List


# O(n) solution using hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_s = 0
        #   keep here sums we can achieve from 0 index
        exists_sum = defaultdict(int)
        #   we always have zero sum with no elements
        exists_sum[0] = 1
        result = 0

        for cur_val in nums:
            #   sum that we need to have in previous subarray
            needed_prev_sum = k - cur_val

            #   sum that we are going to cut from zero index
            sum_to_search = prev_s - needed_prev_sum
            if sum_to_search in exists_sum:
                result += exists_sum[sum_to_search]

            prev_s += cur_val
            exists_sum[prev_s] += 1

        return result


solution = Solution()
nums = [0, 1, 2, -1, 0, -1, 5]
k = 3
print(solution.subarraySum(nums, k))

'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev = 0
        cur = 1

        while cur < len(intervals):
            if intervals[prev][1] >= intervals[cur][0]:
                #   merge two intervals
                intervals[cur][0] = intervals[prev][0]
                intervals[cur][1] = max(intervals[cur][1], intervals[prev][1])
                intervals.pop(prev)
            else:
                prev += 1
                cur += 1
        return intervals


solution = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution.merge(intervals))

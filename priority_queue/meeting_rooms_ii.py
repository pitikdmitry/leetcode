'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #   sort interval by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        #   put intervals in min heap, priority=smallest end time,
        #   before putting new interval, pop all intervals that have already ended
        min_h = []
        max_heap_size = 0

        for interval in intervals:
            start, end = interval[0], interval[1]

            #   pop ended intervals
            while len(min_h) > 0 and min_h[0][0] < start:
                heapq.heappop(min_h)

            heapq.heappush(min_h, (end, start))
            max_heap_size = max(max_heap_size, len(min_h))

        return max_heap_size


solution = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(solution.minMeetingRooms(intervals))

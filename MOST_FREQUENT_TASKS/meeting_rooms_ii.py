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
from queue import PriorityQueue
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #   sort interval by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        #   put intervals in PQ, priority=smallest end time, before putting pop all intervals that has already ended
        pq = PriorityQueue()
        max_pq_size = 0

        for interval in intervals:
            start, end = interval[0], interval[1]

            while pq.qsize() > 0:
                priority, earliest_end_interval = pq.get()
                if earliest_end_interval[1] <= start:
                    continue
                else:
                    #   first el - priority
                    pq.put((earliest_end_interval[1], earliest_end_interval))
                    break

            pq.put((end, interval))
            max_pq_size = max(max_pq_size, pq.qsize())

        return max_pq_size


solution = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(solution.minMeetingRooms(intervals))

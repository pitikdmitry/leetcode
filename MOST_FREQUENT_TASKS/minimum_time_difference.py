'''
Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''
from typing import List


class Solution:
    MINUTES_IN_24_HOURS = 24 * 60

    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return -1

        minutes_list = []
        for point in timePoints:
            hours, minutes = point.split(':')
            point_in_minutes = int(float(hours)) * 60 + int(float(minutes))
            minutes_list.append(point_in_minutes)

        minutes_list.sort()
        smallest_diff = float('inf')
        prev = 0
        cur = 1
        while cur < len(minutes_list):
            cur_diff = minutes_list[cur] - minutes_list[prev]
            smallest_diff = min(smallest_diff, cur_diff)
            prev += 1
            cur += 1

        last_diff = (self.MINUTES_IN_24_HOURS - minutes_list[len(minutes_list) - 1]) + minutes_list[0]
        smallest_diff = min(smallest_diff, last_diff)
        return smallest_diff


s = Solution()
time_points = ["23:59", "00:00"]
print(s.findMinDifference(time_points))

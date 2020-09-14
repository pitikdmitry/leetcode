'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
'''
from math import sqrt
from typing import List


#   Quickselect solution
class Solution:
    def distance_to_origin(self, point: List[int]) -> float:
        return sqrt(point[0] ** 2 + point[1] ** 2)

    #   quicksort partition method
    def partition(self, points: List[List[int]], start: int, end: int) -> int:
        pivot = start
        start += 1

        while start < end:
            while self.distance_to_origin(points[start]) <= self.distance_to_origin(points[pivot]):
                start += 1

            while self.distance_to_origin(points[end]) > self.distance_to_origin(points[pivot]):
                end -= 1

            if start >= end or start >= len(points) or end < 1:
                break

            points[start], points[end] = points[end], points[start]
            start += 1
            end -=1

        points[pivot], points[end] = points[end], points[pivot]
        return end

    def sort(self, points, K, start, end):
        if start > end:
            return []
        m = self.partition(points, start, end)
        if m == K:
            return points[:K]
        elif m < K:
            return self.sort(points, K, m + 1, end)
        else:
            return self.sort(points, K, start, m - 1)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) == K:
            return points
        return self.sort(points, K, 0, len(points) - 1)


solution = Solution()
points = [[1, 3], [-2, 2]]
K = 1
print(solution.kClosest(points, K))

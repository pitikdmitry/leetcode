'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti]
represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance
is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.


Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4,
but we have to return city 3 since it has the greatest number.
'''


#   Floyd-Warshall APSP
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distance_threshold: int) -> int:
        #   setup matrix
        dp = [[float('inf') for j in range(n)] for i in range(n)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == j:
                    dp[i][j] = 0
                    continue

        #   setup weights
        for fr, to, weight in edges:
            dp[fr][to] = weight
            dp[to][fr] = weight

        #   Floyd-Warshall algorithm
        #   try to build path through every node (through k). i - path from, j - path to
        for k in range(n):
            for i in range(len(dp)):
                for j in range(len(dp[0])):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        #   find tasks answer
        min_reachable_cities = float('inf')
        city = 0
        for i in range(len(dp)):
            cur_reachable_cities = 0
            for j in range(len(dp[0])):
                if dp[i][j] <= distance_threshold:
                    cur_reachable_cities += 1

            if cur_reachable_cities <= min_reachable_cities:
                min_reachable_cities = cur_reachable_cities
                city = i

        return city


solution = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(solution.findTheCity(n, edges, distanceThreshold))

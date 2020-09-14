'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
'''
import heapq
from collections import defaultdict
from typing import List


#   Dijkstra's algorithm with priority queue
class Solution:
    def bfs(self, graph, N, K):
        min_h = []
        #   start from node K
        min_h.append((0, K))

        min_times = [float('inf') for _ in range(N + 1)]
        max_delay, nodes_processed = 0, 0
        while len(min_h) > 0:
            time, node = heapq.heappop(min_h)
            if min_times[node] != float('inf'):
                continue

            min_times[node] = time
            max_delay = max(max_delay, time)
            for child, time_to_child in graph[node]:
                heapq.heappush(min_h, (time + time_to_child, child))

            nodes_processed += 1

        if nodes_processed != N:
            return -1
        return max_delay

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for fr, to, weight in times:
            graph[fr].append((to, weight))
            if to not in graph:
                graph[to] = []

        return self.bfs(graph, N, K)


solution = Solution()
times = [[2, 1, 1],
         [2, 3, 1],
         [3, 4, 1]]
N = 4
K = 2
print(solution.networkDelayTime(times, N, K))

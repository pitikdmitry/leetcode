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
from collections import defaultdict
from queue import PriorityQueue
from typing import List, Dict, Tuple


#   Using Dijkstra's algorithm with priority queeu
class Solution:
    def bfs(self, graph: Dict[int, List[Tuple[int, int]]], K: int) -> Tuple[int, int]:
        times_to_reach = {}
        pq = PriorityQueue()
        pq.put((0, K))
        processed_nodes, max_elapsed_time = 0, 0

        while pq.qsize() > 0:
            elapsed_time, node = pq.get()
            #   lazy deleting already processed nodes
            if node in times_to_reach:
                continue

            times_to_reach[node] = elapsed_time
            processed_nodes += 1
            max_elapsed_time = max(max_elapsed_time, elapsed_time)

            neighbours = graph.get(node)
            if neighbours is not None:
                for neighbour, weight in neighbours:
                    pq.put((elapsed_time + weight, neighbour))

        return processed_nodes, max_elapsed_time

    def convert_graph(self, times: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        return graph

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = self.convert_graph(times)

        processed_nodes, max_elapsed_time = self.bfs(graph, K)
        if processed_nodes == N:
            return max_elapsed_time
        return -1


solution = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(solution.networkDelayTime(times, N, K))

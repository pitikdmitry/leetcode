'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
'''


import collections
import heapq
from typing import List, Dict, Tuple


#   Dijkstra's solution. O((V*K + E)*log(V*K)) - because we can visit every node K times (k=max steps)
class Solution:
    def bfs(self, graph: Dict[int, List[Tuple[int, int]]], src: int, dst: int, max_steps: int) -> int:
        min_h, visited = [], set()
        min_h.append((0, src, 0))

        while len(min_h) > 0:
            price, node, steps = heapq.heappop(min_h)
            visited.add((node, steps))

            if steps > max_steps:
                continue

            if node == dst:
                return price

            for child, weight in graph[node]:
                if child not in visited:
                    heapq.heappush(min_h, (price + weight, child, steps + 1))

        return -1

    def convert_graph(self, flights: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            if v not in graph:
                graph[v] = []

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = self.convert_graph(flights)
        return self.bfs(graph, src, dst, K + 1)


solution = Solution()
n = 3
edges = [[3, 2, 1], [2, 11, 1], [2, 7, 2], [7, 8, 2], [11, 12, 1], [12, 8, 1], [8, 15, 2]]
src = 2
dst = 15
k = 4
print(solution.findCheapestPrice(n, edges, src, dst, k))

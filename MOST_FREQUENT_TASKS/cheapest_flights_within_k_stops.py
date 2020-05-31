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
from queue import PriorityQueue
from typing import List, Dict, Tuple


#   Dijkstra algorithm solution, but priority in PQ = current_steps, because we have limit of steps
class Solution:
    def bfs(self, graph: Dict[int, List[Tuple[int, int]]], prices: Dict[int, int], src: int, dst: int, max_steps: int) -> None:
        pq = PriorityQueue()
        start_steps, start_price = 0, 0
        pq.put((start_steps, start_price, src))

        while pq.qsize() > 0:
            steps, price, node = pq.get()
            if steps > max_steps:
                continue

            if node in prices and prices[node] < price:
                continue

            prices[node] = price

            if node == dst:
                continue

            children = graph.get(node)
            if children is None:
                continue

            for child, weight in children:
                pq.put((steps + 1, price + weight, child))

    def convert_graph(self, flights: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = self.convert_graph(flights)
        prices = {}
        max_steps = K + 1
        self.bfs(graph, prices, src, dst, max_steps)
        return prices.get(dst, -1)


solution = Solution()
n = 3
edges = [[3, 2, 1], [2, 11, 1], [2, 7, 2], [7, 8, 2], [11, 12, 1], [12, 8, 1], [8, 15, 2]]
src = 2
dst = 15
k = 4
print(solution.findCheapestPrice(n, edges, src, dst, k))


import collections
from queue import PriorityQueue
from typing import List, Dict, Tuple


#   BFS solution. Go steps by steps, but if we find vertex second time, but now price is smaller - we continue moving
class Solution:
    def bfs(self, graph: Dict[int, List[Tuple[int, int]]], prices: Dict[int, int], src: int, dst: int, max_steps: int) -> None:
        q = []
        steps, start_price = 0, 0
        q.append((src, start_price))

        while len(q) > 0:
            if steps > max_steps:
                break

            for i in range(len(q)):
                node, price = q.pop(0)
                if node in prices and prices[node] <= price:
                    continue

                prices[node] = price
                children = graph.get(node)
                if children is None:
                    continue

                for child, weight in children:
                    q.append((child, price + weight))

            steps += 1

    def convert_graph(self, flights: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = self.convert_graph(flights)
        prices = {}
        max_steps = K + 1
        self.bfs(graph, prices, src, dst, max_steps)
        return prices.get(dst, -1)


solution = Solution()
n = 3
edges = [[3, 2, 1], [2, 11, 1], [2, 7, 2], [7, 8, 2], [11, 12, 1], [12, 8, 1], [8, 15, 2]]
src = 2
dst = 15
k = 4
print(solution.findCheapestPrice(n, edges, src, dst, k))

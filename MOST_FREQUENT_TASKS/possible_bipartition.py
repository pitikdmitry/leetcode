'''
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
'''
from collections import defaultdict
from typing import List, Dict, Tuple


class Solution:
    RED = 0
    BLUE = 1

    #   convert graph from list of edges to adjacency list
    def convert_graph(self, dislikes: List[List[int]]) -> Tuple[Dict[int, List[int]], bool]:
        graph = defaultdict(list)
        has_error = False
        for pair in dislikes:
            if pair[0] == pair[1]:
                has_error = True
                continue

            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        return graph, has_error

    def get_opposite_color(self, color: int) -> int:
        if color == 1:
            return 0
        return 1

    #   instead of visited set we use colors graph and check current color if node in colors
    def dfs(self, node: int, current_color: int, colors: Dict[int, int], graph: Dict[int, List[int]]) -> bool:
        if node in colors:
            if current_color != colors[node]:
                return True
            return False

        colors[node] = current_color

        children = graph.get(node)
        has_error = False
        if children is None:
            return has_error

        for child in children:
            has_error = self.dfs(child, self.get_opposite_color(current_color), colors, graph) or has_error

        return has_error

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph, has_error = self.convert_graph(dislikes)
        if has_error is True:
            return False

        colors = {}
        for node in graph:
            if node in colors:
                continue
            has_error = self.dfs(node, self.RED, colors, graph) or has_error

        return not has_error


solution = Solution()
N = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
print(solution.possibleBipartition(N, dislikes))

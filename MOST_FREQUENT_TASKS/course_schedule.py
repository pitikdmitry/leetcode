'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''
from collections import defaultdict
from typing import List, Dict, Set


class Solution:
    #   we keep track of call stack to find a cycle, we use set for this purpose
    def dfs(self, node: int, graph: Dict[int, List[int]], visited: set, call_stack: Set[int]) -> bool:
        if node is None:
            return False

        if node in call_stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        call_stack.add(node)

        has_cycle = False
        children = graph.get(node)
        if children is not None and len(children) > 0:
            for child in children:
                has_cycle = self.dfs(child, graph, visited, call_stack) or has_cycle

        call_stack.remove(node)
        return has_cycle

    #   transform graph from list of edges to adjacency list
    def transform_graph(self, prerequisites: List[List[int]]) -> Dict[int, List[int]]:
        graph = defaultdict(list)
        for node in prerequisites:
            parent = node[0]
            child = node[1]
            graph[parent].append(child)
        return graph

    #   we need to do DFS and decide if graph has cycle. If there is a cycle we can't complete all courses
    #   graph has representation of edge list
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = self.transform_graph(prerequisites)

        has_cycle = False
        #   start DFS from every node, because we don't know where is root of graph
        for start_node in graph.keys():
            has_cycle = self.dfs(start_node, graph, set(), set()) or has_cycle

        #   if graph has cycle it means that we cant finish all courses
        return not has_cycle


solution = Solution()
prerequisites = [[1, 2], [2, 3], [3, 4], [3, 2], [4, 5]]
num = 5
print(solution.canFinish(num, prerequisites))

'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers,
return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
'''
from typing import List


#   Union find solution
class Solution:
    def __init__(self):
        self.parent = {}

    def make_set(self, val: int) -> None:
        self.parent[val] = val

    #   finding parent, do path compression optimization
    def find_parent(self, val: int) -> int:
        if val == self.parent[val]:
            return val
        parent = self.find_parent(self.parent[val])
        self.parent[val] = parent
        return parent

    def union_two_sets(self, val_a: int, val_b: int) -> None:
        parent_a = self.find_parent(val_a)
        parent_b = self.find_parent(val_b)

        if parent_a == parent_b:
            return

        self.parent[parent_a] = parent_b

    #   if two nodes have one parent -> it makes a cycle
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        last_bad_edge = []
        for node_a, node_b in edges:
            if node_a not in self.parent:
                self.make_set(node_a)

            if node_b not in self.parent:
                self.make_set(node_b)

            parent_a = self.find_parent(node_a)
            parent_b = self.find_parent(node_b)

            if parent_a == parent_b:
                last_bad_edge = [node_a, node_b]
                continue

            self.union_two_sets(node_a, node_b)

        return last_bad_edge


solution = Solution()
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(solution)
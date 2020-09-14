'''
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming
a network where connections[i] = [a, b] represents a connection between computers a and b.
Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers,
and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of
times you need to do this in order to make all the computers connected. If it's not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
'''
from typing import List


class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, val: int) -> None:
        self.parent[val] = val
        self.size[val] = 1

    def get_parent(self, val: int) -> int:
        if self.parent[val] == val:
            return val
        parent = self.get_parent(self.parent[val])
        self.parent[val] = parent
        return parent

    def union(self, val1: int, val2: int) -> int:
        parent1 = self.get_parent(val1)
        parent2 = self.get_parent(val2)
        if parent1 == parent2:
            return False

        if parent1 != parent2 and self.size[parent1] >= self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        elif parent1 != parent2 and self.size[parent1] < self.size[parent2]:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]

        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU()
        #   create disjoint set for every computer
        for i in range(n):
            dsu.make_set(i)

        #   union computers in one set, count not needed connections
        extra_connections = 0
        for fr, to in connections:
            if dsu.union(fr, to) is False:
                extra_connections += 1

        #   count number of connected components
        components = set()
        for val in dsu.parent.keys():
            components.add(dsu.get_parent(val))

        components_amount = len(components)

        #   count connections to union all computers in one set
        needed_connections = components_amount - 1

        if extra_connections < needed_connections:
            return -1
        return needed_connections


solution = Solution()
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(solution.makeConnected(n, connections))

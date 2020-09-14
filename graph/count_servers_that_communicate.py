'''
You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
'''


from typing import List


#   DSU with path compression and union by size
class DSU:
    def __init__(self) -> None:
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

    def union(self, val1: int, val2: int) -> None:
        parent1 = self.get_parent(val1)
        parent2 = self.get_parent(val2)
        if parent1 != parent2 and self.size[parent1] >= self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        elif parent1 != parent2 and self.size[parent1] < self.size[parent2]:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]


#   DSU 2d grid solution
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        dsu = DSU()
        computers_amount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue

                #   add offset for y coordinate and union x and y coordinate
                #   it will allow us to union computers with same x coordinate or same y coordinate
                x, y = i, j + 1000
                if x not in dsu.parent:
                    dsu.make_set(x)
                if y not in dsu.parent:
                    dsu.make_set(y)
                dsu.union(x, y)
                computers_amount += 1

        #   count number of connected components
        alone_sets = 0
        for val, parent in dsu.parent.items():
            if val == parent and dsu.size[val] == 2:
                alone_sets += 1
        return computers_amount - alone_sets


solution = Solution()
grid = [[1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
print(solution.countServers(grid))

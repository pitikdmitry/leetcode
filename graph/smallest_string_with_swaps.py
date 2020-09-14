'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
'''
from collections import defaultdict
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


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU()
        #   create set for every letter
        for i in range(len(s)):
            dsu.make_set(i)

        #   union connected letters
        for x, y in pairs:
            dsu.union(x, y)

        m = defaultdict(list)
        #   map dsu parent to list of valid letters
        for i in range(len(s)):
            parent = dsu.get_parent(i)
            m[parent].append(s[i])

        #   sort lists of strings
        for key, list_val in m.items():
            m[key] = sorted(list_val)

        #   construct final string. Get smallest letter from list by parent
        res = []
        for j in range(len(s)):
            parent = dsu.get_parent(j)
            smallest_letter = m[parent].pop(0)
            res.append(smallest_letter)

        return ''.join(res)


solution = Solution()
s = "dcab"
pairs = [[0, 3], [1, 2]]
print(solution.smallestStringWithSwaps(s, pairs))

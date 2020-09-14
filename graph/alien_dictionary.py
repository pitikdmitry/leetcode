'''
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
'''
from collections import defaultdict
from typing import List, Dict


#   Solution via topological sort Kahn's algorithm
class Solution:
    def create_graph(self, words: List[str]) -> Dict[str, List]:
        word_i = 1
        graph = defaultdict(list)
        #   for two adjacent words if letters are different -> create edge
        while word_i < len(words):
            word_1 = words[word_i - 1]
            word_2 = words[word_i]

            ch_i = 0
            while ch_i < len(word_1) and ch_i < len(word_2):
                ch_1 = word_1[ch_i]
                ch_2 = word_2[ch_i]

                if ch_1 != ch_2:
                    graph[ch_1].append(ch_2)
                    if ch_2 not in graph:
                        graph[ch_2] = []
                    break
                ch_i += 1

            word_i += 1

        return graph

    def alienOrder(self, words: List[str]) -> str:
        graph = self.create_graph(words)

        in_degree = defaultdict(int)
        for key, values in graph.items():
            if key not in in_degree:
                in_degree[key] = 0

            for node in values:
                in_degree[node] += 1

        #   Kahn's algorithm with in_degree array
        q = []
        for key, val in in_degree.items():
            if val == 0:
                q.append(key)

        result = []
        while len(q) > 0:
            node = q.pop(0)
            result.append(node)
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

        return ''.join(result)


solution = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt", "te"]
print(solution.alienOrder(words))

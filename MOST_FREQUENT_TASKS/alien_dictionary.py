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


#   Solution via topological sort Kahn's algorithm via BFS
class Solution:
    def create_graph(self, words: List[str]) -> Dict[str, List]:
        i, j = 0, 1
        graph = defaultdict(list)
        while j < len(words):
            word_1 = words[i]
            word_2 = words[j]

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

            i += 1
            j += 1

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


from collections import defaultdict
from typing import List, Dict


class Solution:
    #   topological sort via dfs
    def dfs(self, node: str, graph: Dict[str, List[str]], visited: set, call_stack: set, topological_order: List[str]):
        if node is None:
            return False

        if node in call_stack:
            return True

        if node in visited:
            return False

        call_stack.add(node)
        visited.add(node)

        children = graph.get(node)
        has_cycle = False
        if children is not None and len(children) > 0:
            for child in children:
                has_cycle = self.dfs(child, graph, visited, call_stack, topological_order) or has_cycle

        call_stack.remove(node)
        topological_order.append(node)
        return has_cycle

    def add_letters_without_edges(self, word: str, graph: Dict[str, List[str]]) -> None:
        for c in word:
            if c not in graph:
                graph[c] = []

    def create_graph(self, words: List[str], graph: Dict[str, List[str]]) -> bool:
        first_word_idx = 0
        second_word_idx = 1
        while second_word_idx < len(words):
            i = 0
            first_word, second_word = words[first_word_idx], words[second_word_idx]

            #   error in alphabet
            if len(first_word) > len(second_word) and (first_word.startswith(second_word) is True):
                return True

            while i < len(first_word) and i < len(second_word):
                if first_word[i] != second_word[i]:
                    graph[first_word[i]].append(second_word[i])
                    break
                i += 1
            first_word_idx += 1
            second_word_idx += 1

        for word in words:
            self.add_letters_without_edges(word, graph)

        return False

    def alienOrder(self, words: List[str]) -> str:
        if words is None or len(words) == 0 or len(words[0]) == 0:
            return ''

        graph = defaultdict(list)
        found_error = self.create_graph(words, graph)
        if found_error is True:
            return ''

        #   starting topological sort
        topological_order = []
        visited = set()
        for node in graph.keys():
            has_cycle = self.dfs(node, graph, visited, set(), topological_order)
            if has_cycle is True:
                return ''

        return ''.join(reversed(topological_order))


solution = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt", "te"]
print(solution.alienOrder(words))



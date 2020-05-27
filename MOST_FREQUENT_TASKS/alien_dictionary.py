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


from collections import defaultdict
from typing import List, Dict


#   Solution via topological sort Kahn's algorithm via BFS
class Solution:
    def add_letters_without_edges(self, word: str, graph: Dict[str, List[str]], in_degree: Dict[str, int]) -> None:
        for c in word:
            if c not in graph:
                graph[c] = []
            if c not in in_degree:
                in_degree[c] = 0

    def create_graph(self, words: List[str], graph: Dict[str, List[str]], in_degree: Dict[str, int]) -> None:
        first_word_idx = 0
        second_word_idx = 1
        while second_word_idx < len(words):
            i = 0
            first_word, second_word = words[first_word_idx], words[second_word_idx]

            while i < len(first_word) and i < len(second_word):

                if first_word[i] != second_word[i]:
                    graph[first_word[i]].append(second_word[i])

                    in_degree[second_word[i]] += 1
                    if first_word[i] not in in_degree:
                        in_degree[first_word[i]] = 0
                    break
                i += 1
            first_word_idx += 1
            second_word_idx += 1

        for word in words:
            self.add_letters_without_edges(word, graph, in_degree)

    def alienOrder(self, words: List[str]) -> str:
        if words is None or len(words) == 0 or len(words[0]) == 0:
            return ''

        #   create graph
        graph, in_degree = defaultdict(list), defaultdict(int)
        self.create_graph(words, graph, in_degree)

        #   do bfs
        topological_order = []
        q = []
        for node, degree in in_degree.items():
            if degree == 0:
                q.append(node)

        while len(q) > 0:
            node = q.pop(0)
            topological_order.append(node)

            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

        return ''.join(topological_order)


solution = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt", "te"]
print(solution.alienOrder(words))

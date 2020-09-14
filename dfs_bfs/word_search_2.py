from typing import List


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def add_word(self, word):
        node = self.root
        for idx, c in enumerate(word):
            if c not in node.children:
                new_node = TrieNode(c)
                node.children[c] = new_node

            node = node.children[c]
        node.is_word = True


class Solution:
    def dfs(self, board, i, j, trie_node, visited, result, cur_word):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        if (i, j) in visited:
            return

        ch = board[i][j]
        if ch in trie_node.children:
            visited.add((i, j))

            cur_word += ch
            node = trie_node.children[ch]
            if node.is_word is True:
                result.add(cur_word)

            self.dfs(board, i + 1, j, node, visited, result, cur_word)
            self.dfs(board, i - 1, j, node, visited, result, cur_word)
            self.dfs(board, i, j + 1, node, visited, result, cur_word)
            self.dfs(board, i, j - 1, node, visited, result, cur_word)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                self.dfs(board, i, j, trie.root, visited, result, '')
        return list(result)


solution = Solution()
board = [
    ["a", "b"],
    ["c", "d"]
]
words = ["cdba"]
print(solution.findWords(board, words))

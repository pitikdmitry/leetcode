'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children = {}
        self.is_word = False


#   Trie
class WordDictionary:

    def __init__(self) -> None:
        self.root = Node('')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) == 0:
            return

        node = self.root
        for c in word:
            if c not in node.children:
                new_node = Node(c)
                node.children[c] = new_node

            node = node.children[c]

        node.is_word = True

    def search_helper(self, word: str, start: int, node: Node) -> bool:

        for i in range(start, len(word)):
            c = word[i]

            result = False
            #   do recursive calls to all children
            if c == '.':
                for child_node in node.children.values():
                    result |= self.search_helper(word, i + 1, child_node)

                return result

            if c not in node.children:
                return False
            node = node.children[c]

        if node.is_word is True:
            return True
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_helper(word, 0, self.root)


dictionary = WordDictionary()
dictionary.addWord("bad")
dictionary.addWord("dad")
dictionary.addWord("mad")
print(dictionary.search("pad"))
print(dictionary.search("bad"))
print(dictionary.search(".ad"))
print(dictionary.search("b.."))

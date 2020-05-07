'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        dummy.next = head
        dummy_copy = Node(-1)

        node = dummy
        node_copy = dummy_copy

        visited = {}
        while node is not None:
            next_node = node.next
            if next_node is not None:
                if next_node not in visited:
                    new_node = Node(next_node.val)
                    visited[next_node] = new_node

                node_copy.next = visited[next_node]

            random_node = node.random
            if random_node is not None:
                if random_node not in visited:
                    new_node = Node(random_node.val)
                    visited[random_node] = new_node

                node_copy.random = visited[random_node]

            node = node.next
            node_copy = node_copy.next

        return dummy_copy.next

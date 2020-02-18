'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_helper(self, l1: ListNode, l2: ListNode, root: ListNode, current_node: ListNode):
        if l1 is None and l2 is None:
            return root
        if l1 is None or (l1 is not None and l2 is not None and l1.val >= l2.val):
            new_node = ListNode(l2.val)
            if current_node is not None:
                current_node.next = new_node
            if root is None:
                root = new_node
            return self.merge_helper(l1, l2.next, root, new_node)

        elif l2 is None or (l1 is not None and l2 is not None and l1.val < l2.val):
            new_node = ListNode(l1.val)
            if current_node is not None:
                current_node.next = new_node
            if root is None:
                root = new_node
            return self.merge_helper(l1.next, l2, root, new_node)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.merge_helper(l1, l2, None, None)

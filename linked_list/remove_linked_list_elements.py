'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_helper(self, head: ListNode, val: int):
        cur = head
        next_node = head.next

        while next_node is not None:
            if next_node.val == val:
                cur.next = next_node.next
                next_node = next_node.next
            else:
                cur = cur.next
                next_node = next_node.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        self.remove_helper(dummy, val)
        return dummy.next

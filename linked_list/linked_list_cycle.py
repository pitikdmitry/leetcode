'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if slow is None:
            return False

        fast = slow.next
        while fast is not None and fast is not slow:
            slow = slow.next
            fast = fast.next

            if fast is None:
                return False

            fast = fast.next

        if fast is None:
            return False
        return True

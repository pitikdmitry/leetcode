'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        if cur is None:
            return cur
        next = head.next
        if next is None:
            return cur

        cur.next = next.next
        next.next = cur

        new_next_head = self.swapPairs(cur.next)
        cur.next = new_next_head

        return next

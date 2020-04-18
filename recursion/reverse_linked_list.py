'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def reverse(self, prev: ListNode, cur: ListNode) -> ListNode:
        if cur is None:
            return prev

        next = cur.next
        cur.next = prev
        return self.reverse(cur, next)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(None, head)

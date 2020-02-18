'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, prev, cur):
        if cur is None:
            return prev

        next = cur.next
        cur.next = prev
        return self.reverse(cur, next)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(None, head)

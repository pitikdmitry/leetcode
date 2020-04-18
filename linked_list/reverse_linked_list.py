'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def reverse(self, prev, cur) -> ListNode:
        if cur is None:
            return prev

        next = cur.next
        cur.next = prev
        return self.reverse(cur, next)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(None, head)

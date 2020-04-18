'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def remove_helper(self, head: ListNode, n: int) -> int:
        if head is None:
            return 0

        result = self.remove_helper(head.next, n)
        if result == n:
            if head.next is not None:
                head.next = head.next.next

        return result + 1

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        self.remove_helper(dummy, n)
        return dummy.next

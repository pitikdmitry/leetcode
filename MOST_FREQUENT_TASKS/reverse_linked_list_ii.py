'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, p: int, q: int) -> ListNode:
        i, prev, cur = 1, None, head
        #   finding p - 1 node
        while i != p:
            i += 1
            prev = cur
            cur = cur.next

        before_p = prev
        last_in_p_q_interval = cur

        #   reverse
        prev = None
        while i <= q:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next
            i += 1

        #   connect parts, assign new head if needed
        if before_p is not None:
            before_p.next = prev
        else:
            head = prev

        last_in_p_q_interval.next = cur
        return head

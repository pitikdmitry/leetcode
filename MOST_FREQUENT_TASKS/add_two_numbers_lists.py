'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        carry = 0
        current_node = dummy
        while l1 is not None or l2 is not None:
            s = carry
            if l1 is not None:
                s += l1.val
                l1 = l1.next

            if l2 is not None:
                s += l2.val
                l2 = l2.next

            if s >= 10:
                carry = 1
                s %= 10
            else:
                carry = 0

            new_node = ListNode(s)
            current_node.next = new_node
            current_node = current_node.next

        if carry == 1:
            new_node = ListNode(carry)
            current_node.next = new_node

        return dummy.next

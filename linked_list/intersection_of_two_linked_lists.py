'''Write a program to find the node at which the intersection of two singly linked lists begins.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def gen_length(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l_1 = self.gen_length(headA)
        l_2 = self.gen_length(headB)

        if l_1 > l_2:
            longest_list_pointer = headA
            shortest_list_pointer = headB
        else:
            longest_list_pointer = headB
            shortest_list_pointer = headA

        diff = abs(l_2 - l_1)
        for i in range(diff):
            longest_list_pointer = longest_list_pointer.next

        while longest_list_pointer is not None and shortest_list_pointer is not None \
            and longest_list_pointer is not shortest_list_pointer:
            longest_list_pointer = longest_list_pointer.next
            shortest_list_pointer = shortest_list_pointer.next

        if longest_list_pointer is None or shortest_list_pointer is None:
            return None

        return longest_list_pointer

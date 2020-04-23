# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


#   merge sort
class Solution:
    def _find_center(self, head: ListNode) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, node_1: ListNode, node_2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur_node = dummy

        while node_1 is not None and node_2 is not None:
            if node_1.val <= node_2.val:
                cur_node.next = node_1
                node_1 = node_1.next
            else:
                cur_node.next = node_2
                node_2 = node_2.next

            cur_node = cur_node.next

        while node_1 is not None:
            cur_node.next = node_1
            node_1 = node_1.next
            cur_node = cur_node.next

        while node_2 is not None:
            cur_node.next = node_2
            node_2 = node_2.next
            cur_node = cur_node.next

        return dummy.next

    def sortList(self, head: ListNode) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        center = self._find_center(head)
        right_head = center.next
        center.next = None

        res_1 = self.sortList(head)
        res_2 = self.sortList(right_head)
        return self._merge(res_1, res_2)

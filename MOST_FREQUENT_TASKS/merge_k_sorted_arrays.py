'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#   merge by two (divide and conquer)
class Solution:
    def merge_two_lists(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        def add_value_to_list(head: ListNode, tail: ListNode, val) -> tuple:
            new_node = ListNode(val)
            tail.next = new_node
            tail = tail.next
            return head, tail

        result_head = ListNode(-1)
        result_tail = result_head

        while head_1 is not None and head_2 is not None:
            if head_1.val < head_2.val:
                result_head, result_tail = add_value_to_list(result_head, result_tail, head_1.val)
                head_1 = head_1.next
            else:
                result_head, result_tail = add_value_to_list(result_head, result_tail, head_2.val)
                head_2 = head_2.next

        if head_1 is not None:
            result_tail.next = head_1

        elif head_2 is not None:
            result_tail.next = head_2

        return result_head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        i = 0
        j = 1
        while len(lists) > 1:
            if (i == len(lists) - 1 and j == len(lists)) or i >= len(lists):
                i = 0
                j = 1

            l_1 = lists[i]
            l_2 = lists[j]
            result_list = self.merge_two_lists(l_1, l_2)
            lists[i] = result_list
            lists.pop(j)

        return lists[0]


#   Merge one by one
class Solution:
    def add_to_list(self, head: ListNode, tail: ListNode, val) -> tuple:
        new_node = ListNode(val)

        if head is None:
            head = new_node
            tail = head
            return head, tail

        tail.next = new_node
        tail = tail.next
        return head, tail

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        tail = None
        while len(lists) > 0:
            min_el_list_idx = float('inf')
            min_el = float('inf')
            i = 0

            while i < len(lists):
                current_list_head = lists[i]
                if current_list_head is None:
                    lists.pop(i)
                    continue

                element = current_list_head.val
                if element < min_el:
                    min_el = element
                    min_el_list_idx = i

                i += 1

            if min_el != float('inf'):
                head, tail = self.add_to_list(head, tail, min_el)
                lists[min_el_list_idx] = lists[min_el_list_idx].next

        return head

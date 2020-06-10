'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def count_cycle_length(self, start_node: ListNode) -> int:
        runner = start_node.next
        length = 1
        while runner != start_node:
            runner = runner.next
            length += 1

        return length

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        #   detect a cycle + mode slow node somewhere in cycle
        slow, fast = head, head.next
        while slow != fast:
            if slow is None or fast is None:
                return None

            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next

        #   calculating cycle length
        cycle_length = self.count_cycle_length(slow)

        #   start two new pointers from start
        slow, fast = head, head

        #   move one pointer on cycle_length ahead
        for i in range(cycle_length):
            fast = fast.next

        #   move slow and fast pointer by one step until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(solution.detectCycle(head).val))

# head.next.next.next.next.next.next = head.next.next.next
# print("LinkedList cycle start: " + str(solution.detectCycle(head).val))

'''
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node. If you want to use the doubly linked list,
you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list.
After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list.
If index equals to the length of linked list, the node will be appended to the end of linked list.
If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
'''


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self._root = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._root
        for i in range(index):
            if node is None:
                return -1
            node = node.next

        if node is not None:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)

        if self._root is None:
            self._root = new_node
        else:
            new_node.next = self._root
            self._root = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)

        if self._root is None:
            self._root = new_node
        else:
            prev = self._root
            while prev.next is not None:
                prev = prev.next

            prev.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        prev = self._root
        counter = 1
        while counter < index:
            if prev is None:
                return
            prev = prev.next
            counter += 1

        if prev is None:
            return

        new_node = Node(val)

        new_node.next = prev.next
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self._root is not None:
                self._root = self._root.next
            return

        prev = self._root
        counter = 1
        while counter < index:
            if prev is None:
                return

            prev = prev.next
            counter += 1

        if prev is None:
            return
        if prev.next is None:
            return

        prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

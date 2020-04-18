'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def validate(self, node: Optional[TreeNode], max_val: float, min_val: float) -> bool:
        if node is None:
            return True

        if node.val >= max_val or node.val <= min_val:
            return False
        if node.left is not None and node.left.val >= node.val:
            return False
        if node.right is not None and node.right.val <= node.val:
            return False
        res_1 = self.validate(node.left, node.val, min_val)
        res_2 = self.validate(node.right, max_val, node.val)
        return res_1 and res_2

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, float('inf'), float('-inf'))

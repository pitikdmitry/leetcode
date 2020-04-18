'''
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node.
If such node doesn't exist, you should return NULL.
'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if node is None:
            return None

        if node.val == val:
            return node

        res_l = self.searchBST(node.left, val)
        if res_l is not None:
            return res_l

        res_r = self.searchBST(node.right, val)
        return res_r

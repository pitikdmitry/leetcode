'''
Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def same_tree(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        res = self.same_tree(left.left, right.left) and self.same_tree(left.right, right.right)
        return res

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        res = self.same_tree(s, t)
        res_1 = self.isSubtree(s.left, t)
        res_2 = self.isSubtree(s.right, t)
        return res or res_1 or res_2

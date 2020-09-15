'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


#   post order recursive solution
class Solution:
    def __init__(self):
        self._ans = None

    def helper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if root is None:
            return False

        res_1 = self.helper(root.left, p, q)
        res_2 = self.helper(root.right, p, q)
        #   we have found lca if p is in left subtree and q is in right subtree or vice versa
        if res_1 is True and res_2 is True:
            self._ans = root

        #   or if one node is in subtree and second node equals to current node
        if (res_1 is True or res_2 is True) and (root.val == p.val or root.val == q.val):
            self._ans = root

        #   we assume that both p and q are in left subtree or in right subtree
        if root.val == p.val or root.val == q.val:
            return True

        return res_1 or res_2

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.helper(root, p, q)
        return self._ans

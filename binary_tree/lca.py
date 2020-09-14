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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#   post order solution
class Solution:
    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        if root is None:
            return False

        res_1 = self.helper(root.left, p, q)
        res_2 = self.helper(root.right, p, q)
        stay_on_value = False
        if root.val == p.val or root.val == q.val:
            stay_on_value = True

        sum_res = int(res_1) + int(res_2) + int(stay_on_value)
        if sum_res >= 2:
            self.ans = root

        if root.val == p.val or root.val == q.val:
            return True

        return res_1 or res_2

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.helper(root, p, q)
        return self.ans

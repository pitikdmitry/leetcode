'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#   can be optimized with Hashmap for searching elements (instead of linear search index() )
class Solution:
    def helper(self, pre_order: List, in_order: List, left: int, right: int, pre_order_cur_position: int):
        if left > right:
            return None
        if left == right:
            return TreeNode(pre_order[pre_order_cur_position])

        in_order_position = in_order.index(pre_order[pre_order_cur_position])
        node = TreeNode(pre_order[pre_order_cur_position])

        in_order_left_count = in_order_position - left
        node.left = self.helper(pre_order, in_order, left, in_order_position - 1, pre_order_cur_position + 1)

        node.right = self.helper(pre_order, in_order, in_order_position + 1, right, pre_order_cur_position + in_order_left_count + 1)
        return node

    def buildTree(self, pre_order: List[int], in_order: List[int]) -> TreeNode:
        if len(pre_order) == 0:
            return None
        return self.helper(pre_order, in_order, 0, len(pre_order) - 1, 0)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
head = s.buildTree(preorder, inorder)
print(head)

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
from typing import List, Optional


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


#   We have left and right indexes of pre order.
#   On next step we need to find most left element of pre_order in in_order array. It's position in in_order allows us
#   to determine left and right subtrees in pre_order
class Solution:
    def helper(self, pre_order: List, in_order: List, left: int, right: int, pre_order_cur_position: int) -> Optional[TreeNode]:
        if left > right:
            return None
        if left == right:
            return TreeNode(pre_order[pre_order_cur_position])

        #   find left element in in_order
        in_order_position = in_order.index(pre_order[pre_order_cur_position])
        #   create root of subtree
        node = TreeNode(pre_order[pre_order_cur_position])

        #   process left subtree
        in_order_left_count = in_order_position - left
        node.left = self.helper(pre_order, in_order, left, in_order_position - 1, pre_order_cur_position + 1)

        #   process right subtree
        node.right = self.helper(pre_order, in_order, in_order_position + 1, right,
                                 pre_order_cur_position + in_order_left_count + 1)
        return node

    def buildTree(self, pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
        if len(pre_order) == 0:
            return None
        return self.helper(pre_order, in_order, 0, len(pre_order) - 1, 0)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
head = s.buildTree(preorder, inorder)
print(head.val)

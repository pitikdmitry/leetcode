'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root):
        stack = []
        printed_levels = set()
        result = []
        stack.append((root, 0))

        while len(stack) > 0:
            node, level = stack.pop(len(stack) - 1)
            if node is None:
                continue

            if level not in printed_levels:
                result.append(node.val)
                printed_levels.add(level)

            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

        return result

    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.dfs(root)

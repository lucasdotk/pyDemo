# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    length = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(node: TreeNode, i):
            if not node:
                if i > self.length:
                    self.length = i
                return
            recursive(node.left, i + 1)
            recursive(node.right, i + 1)

        recursive(root, 0)

        return self.length

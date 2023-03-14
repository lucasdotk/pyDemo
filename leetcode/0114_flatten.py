# Definition for a binary tree node.
from queue import Queue
from typing import Optional

from leetcode.utils import generate, inorder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def dfs(node: TreeNode):
            if not node:
                return
            res.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        for i in range(len(res) - 1):
            node = res[i]
            node.left = None
            node.right = res[i + 1]


root = generate([1, 2, 5, 3, 4, None, 6])
s = Solution()
s.flatten(root)
print(root.val)
print(root.right.val)
print(root.right.right.val)
print(root.right.right.right.val)

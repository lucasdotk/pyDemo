# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursive(node: TreeNode):
            if not node:
                return
            res.append(node.val)
            recursive(node.left)
            recursive(node.right)

        recursive(root)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        res = []

        while root or len(stack) > 0:
            while root:
                # res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


demo = generate([1, None, 2, 3])
demo = generate([2, 1, 3, None, 4])
s = Solution()
print(s.preorderTraversal2(demo))

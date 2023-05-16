# Definition for a binary tree node.
import sys
from collections import deque
from typing import Optional
from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []

        def recursive(node: TreeNode):
            if not node:
                return
            recursive(node.left)
            res.append(node.val)
            recursive(node.right)

        recursive(root)
        last = res[0]
        for num in res[1:]:
            if num <= last:
                return False
            last = num
        return True

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        last = -(2 << 31)

        def recursive(node: TreeNode):
            if not node:
                return True

            if not recursive(node.left):
                return False

            nonlocal last
            if last >= node.val:
                return False
            last = node.val

            if not recursive(node.right):
                return False
            return True

        return recursive(root)

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        """
        optimize by using stack monitor inorder dfs
        """

        q = deque()
        last = -sys.maxsize

        while root or len(q) > 0:
            while root:
                q.append(root)
                root = root.left
            root = q.pop()
            if last > root.val:
                return False
            last = root.val
            root = root.right

        return True


root = generate([2, 1, 3])
# root = generate([1, 1])

s = Solution()
print(s.isValidBST2(root))
print(s.isValidBST3(root))

# Definition for a binary tree node.
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


root = generate([2, 1, 3])
# root = generate([1, 1])

s = Solution()
print(s.isValidBST2(root))

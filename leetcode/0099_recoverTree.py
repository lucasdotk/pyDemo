# Definition for a binary tree node.
from typing import Optional

from leetcode.utils import generate, inorder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def recursive(node: TreeNode):
            if not node:
                return
            recursive(node.left)
            res.append(node.val)
            recursive(node.right)

        recursive(root)

        index1, index2 = -1, -1
        for i in range(1, len(res)):
            if res[i - 1] > res[i]:
                index2 = i
                if index1 == -1:
                    index1 = i - 1
                else:
                    break
        num1, num2 = res[index1], res[index2]

        def recover(node: TreeNode):
            if not node:
                return
            recover(node.left)
            nonlocal num1, num2
            if node.val == num1:
                node.val = num2
            elif node.val == num2:
                node.val = num1
            recover(node.right)

        recover(root)


root = generate([1, 3, None, None, 2])
print(inorder(root))
s = Solution()
s.recoverTree(root)
print(inorder(root))

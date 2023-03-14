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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursive(node: TreeNode):
            if not node:
                return
            recursive(node.left)
            res.append(node.val)
            recursive(node.right)

        recursive(root)
        return res

    def inorder(self, root:Optional[TreeNode]) -> List[int]:
        """
        使用栈完成中序遍历
        """
        stack = deque()
        res = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


alist = [1, None, 2, 3]


test = generate(alist)
print(test.val)
print(test.left)
print(test.right.val)
print(test.right.left.val)

s = Solution()
print(s.inorderTraversal(test))
print(s.inorder(test))

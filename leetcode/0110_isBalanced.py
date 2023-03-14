# Definition for a binary tree node.
import sys
from typing import Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_value = sys.maxsize
    max_value = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)


root = generate([3, 9, 20, None, None, 15, 7])
root = generate([1, 2, 2, 3, 3, None, None, 4, 4])
root = generate([1, 2, 3, 4, 5, 6, None, 8])
s = Solution()
print(s.isBalanced(root))

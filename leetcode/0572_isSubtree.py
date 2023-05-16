# Definition for a binary tree node.
from typing import Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            return node1.val == node2.val and is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)

        if not root:
            return False
        return is_equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()
print(s.isSubtree(generate([3, 4, 5, 1, 2]), generate([4, 1, 2])))

# Definition for a binary tree node.
from typing import Optional
from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right):
            return True
        return False


s = Solution()
p = [1, 2]
q = [1, None, 2]
print(s.isSameTree(generate(p), generate(q)))

# Definition for a binary tree node.
from collections import deque
from typing import Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        q = deque()
        while root or len(q) > 0:
            while root:
                q.append(root)
                root = root.left
            root = q.pop()
            i += 1
            if i == k:
                return root.val
            root = root.right

        # def dfs(node: TreeNode):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     self.i += 1
        #     if self.i == k:
        #
        #     dfs(node.right)

aa = [2,3,1]
aa.sort()

root = generate([3, 1, 4, None, 2])
root = generate([5, 3, 6, 2, 4, None, None, 1])
k = 3
s = Solution()
print(s.kthSmallest(root, k))

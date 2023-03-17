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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while len(q) > 0:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res


root = generate([3, 9, 20, None, None, 15, 7])
s = Solution()
print(s.levelOrder(root))

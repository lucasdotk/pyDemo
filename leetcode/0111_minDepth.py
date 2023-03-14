# Definition for a binary tree node.
import sys
from collections import deque
from queue import Queue
from typing import Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        使用深度遍历优先，占用内容多于bfs
        @param root:
        @return:
        """
        if not root:
            return 0
        res = sys.maxsize

        def dfs(node: TreeNode, i: int):
            if node:
                i += 1
                if not node.left and not node.right:
                    nonlocal res
                    res = min(res, i)
                dfs(node.left, i)
                dfs(node.right, i)

        dfs(root, 0)
        return res

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        """
        使用Queue导致执行时间长
        @param root:
        @return:
        """
        if not root:
            return 0

        q = Queue()
        q.put(root)
        i = 0
        res = sys.maxsize
        while not q.empty():
            i += 1
            for _ in range(q.qsize()):
                node = q.get()

                if not node.left and not node.right:
                    res = min(res, i)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return res

    def minDepth3(self, root: Optional[TreeNode]) -> int:
        """
        deque + bfs达到了速度和内存占用都比较优的情况
        @param root:
        @return:
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        i = 0
        res = sys.maxsize
        while len(q) > 0:
            i += 1
            for _ in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    res = min(res, i)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


root = generate([1, 2, 3, 4, 5])
s = Solution()
print(s.minDepth2(root))

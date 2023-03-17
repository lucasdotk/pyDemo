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
    max_num = - sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            # 需要注意的是，node是必需包含的，对于在左边和右边，我们选择增益最多的，可能是左边，也可能是右边，也可能两边都要
            self.max_num = max(self.max_num, node.val + max(left, 0) + max(right, 0))
            # 返回的是该去向何方，只取当前节点？去左边好？去右边好？
            return node.val + max(left, right, 0)

        dfs(root)
        return self.max_num


root = generate([-10, 9, 20, None, None, 15, 7])
# root = generate([-3])
s = Solution()
print(s.maxPathSum(root))

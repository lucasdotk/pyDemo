# Definition for a binary tree node.
from typing import Optional
from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(node: TreeNode, value: int):
            if node:
                value += node.val
                if value == targetSum and not node.left and not node.right:
                    return True
                if recursive(node.left, value) or recursive(node.right, value):
                    return True
            return False

        if not root:
            return False
        return recursive(root, 0)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        leetCode官方题解
        @param root:
        @param targetSum:
        @return:
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum2(root.left, targetSum - root.val) or self.hasPathSum2(root.right, targetSum - root.val)


s = Solution()
value_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22
root = generate(value_list)
print(s.hasPathSum(root, targetSum))
print(s.hasPathSum2(root, targetSum))

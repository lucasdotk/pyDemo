# Definition for a binary tree node.
from copy import copy
from typing import List, Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        1使用copy每次创建数组导致空间占用大，2使用sum需要每次计算数组所有数的和
        @param root:
        @param targetSum:
        @return:
        """
        res = []

        def recursive(node: TreeNode, value_list: List[int]):
            if node:
                value_list.append(node.val)
                if sum(value_list) == targetSum and not node.left and not node.right:
                    res.append(value_list)
                recursive(node.left, copy(value_list))
                recursive(node.right, copy(value_list))

        recursive(root, [])
        return res

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        官方题解：1每次dfs只传值，2使用减法不用sum，3判断是优先判断node的左右子树是否为空
        @param root:
        @param targetSum:
        @return:
        """
        res = []
        path = []

        def recursive(node: TreeNode, value: int):
            if node:
                path.append(node.val)
                value -= node.val
                if not node.left and not node.right and value == 0:
                    res.append(path[:])
                recursive(node.left, value)
                recursive(node.right, value)
                path.pop()

        recursive(root, targetSum)
        return res


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = generate(root)
s = Solution()
print(s.pathSum(root, 22))

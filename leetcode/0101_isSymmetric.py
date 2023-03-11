# Definition for a binary tree node.
from copy import copy
from typing import Optional

from leetcode.utils import generate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(x: TreeNode, y: TreeNode):
            if not x and not y:
                return True
            elif not x or not y:
                return False

            if recursive(x.left, y.right) and x.val == y.val and recursive(x.right, y.left):
                return True
            return False

        recursive(root.left, root.right)


res = []


def recu(node: TreeNode, i: int):
    """
    记录node所在的层级，可以使得即使左右子树的中序遍历的结果【List[int]】相同，也能探测到结构的不同
    """
    if not node:
        res.append(101 + i)
        return
    recu(node.left, i + 1)
    res.append(node.val)
    recu(node.right, i + 1)


root = generate([1, 2, 2, 2, None, 2])
root = generate([1, 2, 2, 2, None, None, 2])
recu(root.left, 0)
print(res)
res = []
recu(root.right, 0)
print(res)

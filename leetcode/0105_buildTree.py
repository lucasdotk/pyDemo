from queue import Queue
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_tree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None

            # 从前序中获取根节点的值，获取根节点在中序中的位置，并构建根节点
            root_value = preorder[pre_left]
            in_index = in_dict[root_value]
            root = TreeNode(root_value)

            # 左子树的节点个数
            right_tree_len = in_index - in_left

            root.left = build_tree(pre_left + 1, pre_left + right_tree_len, in_left, in_index - 1)
            root.right = build_tree(pre_left + right_tree_len + 1, pre_right, in_index + 1, in_right)

            return root

        m = len(preorder)
        n = len(inorder)

        in_dict = {}
        for i, value in enumerate(inorder):
            in_dict[value] = i

        return build_tree(0, m - 1, 0, n - 1)

    def print_list_from_tree(self, root: TreeNode):
        q = Queue()
        q.put(root)
        res = []
        while q.qsize():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

            res.append(node.val)
        return res


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
so = Solution()
r = so.buildTree(preorder, inorder)
print(so.print_list_from_tree(r))

# Definition for a binary tree node.
from queue import Queue
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursive(node: TreeNode):
            if not node:
                return
            recursive(node.left)
            res.append(node.val)
            recursive(node.right)

        recursive(root)
        return res


alist = [1, None, 2, 3]


def generate(node_list: List[int]) -> TreeNode:
    if len(node_list) == 0:
        return TreeNode()

    q = Queue()
    [q.put(i) for i in node_list]

    node_q = Queue()
    root = TreeNode(val=q.get())
    node_q.put(root)
    while not node_q.empty():

        node = node_q.get()
        if not q.empty():
            left = q.get()
            if left:
                left_node = TreeNode(val=left)
                node.left = left_node
                node_q.put(left_node)

        if not q.empty():
            right = q.get()
            if right:
                right_node = TreeNode(val=right)
                node.right = right_node
                node_q.put(right_node)

    return root

test = generate(alist)
print(test.val)
print(test.left)
print(test.right.val)
print(test.right.left.val)

s = Solution()
print(s.inorderTraversal(test))

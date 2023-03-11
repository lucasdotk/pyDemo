import sys
from queue import Queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        v_list = []

        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

            v_list.append(node.val)

        v_list.sort()
        print(v_list)
        before = v_list[0]
        min_value = sys.maxsize
        for i in v_list[1:]:
            if i - before < min_value:
                min_value = i - before
            before = i
        return min_value


s = Solution()
# node1 = TreeNode(4)
# node2 = TreeNode(2)
# node3 = TreeNode(6)
# node4 = TreeNode(1)
# node5 = TreeNode(3)
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

node1 = TreeNode(27)
node2 = TreeNode(34)
node3 = TreeNode(58)
node4 = TreeNode(50)
node5 = TreeNode(44)
node1.right = node2
node2.right = node3
node3.left = node4
node4.left = node5

print(s.minDiffInBST(node1))

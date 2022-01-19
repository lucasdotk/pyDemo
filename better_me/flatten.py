#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/11/10 4:16 下午 
# @Author  : kuangchao@zingfront.com
# @File    : flatten.py
# @Description :


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


node1 = Node(1, None, None, None)
node2 = Node(2, None, None, None)
node3 = Node(3, None, None, None)
node4 = Node(4, None, None, None)
node5 = Node(5, None, None, None)
node6 = Node(6, None, None, None)
node7 = Node(7, None, None, None)

node1.next = node2

node2.prev = node1
node2.next = node3
node2.child = node4

node3.prev = node2

node4.next = node5
node4.prev = node2
node4.child = node6

node5.prev = node4

node6.prev = node4
node6.next = node7

node7.prev = node6


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(node: Node) -> Node:

            cur = node
            # 每层的结束或进入子节点的点
            last = None

            while cur:

                if cur.child:

                    # 获取子节点所在列的最后一个节点
                    child_last = dfs(cur.child)

                    child_last.next = cur.next
                    cur.next.prev = child_last

                    cur.child = None

                    if cur.next:
                        last = child_last
                else:
                    last = cur

                cur = cur.next

            return last

        dfs(head)

s = Solution()
s.flatten(node1)

current = node1
while current:
    print(current.val)
    print('hello')
    current = current.next

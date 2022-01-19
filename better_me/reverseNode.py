#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/12/31 3:30 下午 
# @Author  : kuangchao@zingfront.com
# @File    : reverseNode.py
# @Description :
class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.next = nxt


def flutter(node: Node, start, end):
    count = 0
    prev = None
    while node:
        if start <= count <= end:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        else:
            prev = node
            node = node.next
        count += 1
    return prev


def x(node: Node):
    if node is None:
        return

    if node:
        node = x(node.next)


node1 = Node(1, None)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)

node = flutter(node4, 0, 3)
while node:
    print(node.val)
    node = node.next

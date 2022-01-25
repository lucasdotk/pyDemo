#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/12/31 3:30 下午 
# @Author  : kuangchao@zingfront.com
# @File    : reverseNode.py
# @Description :


class Node:
    val = 0
    next = None

    def __init__(self, val):
        self.val = val


def flutter(node: Node, start: int, end: int):
    count = 0
    prev = None
    first_skip = False if start == 0 else True
    while node:
        if start <= count <= end:
            # 防止出现两个节点互指
            if first_skip:
                prev = node
                node = node.next
                prev.next = None
                first_skip = False
                continue
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        else:
            prev = node
            node = node.next
        count += 1
    return prev


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = flutter(node1, 1, 3)
for n in [node1, node2, node3, node4]:
    if n.next:
        print("cur是{}，next是{}".format(n.val, n.next.val))
    else:
        print("cur是{}，next是None".format(n.val))

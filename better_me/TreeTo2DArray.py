#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/25 10:04 上午 
# @Author  : kuangchao@zingfront.com
# @File    : TreeTo2DArray.py
# @Description :
from queue import Queue


class Tree:
    value = 0
    left = None
    right = None


def getArray(tree: Tree):
    ele_list = Queue()
    ele_list.put(tree)
    last = tree
    n_last = None

    res = []
    tmp = []
    while ele_list.qsize() > 0:
        cur = ele_list.get()
        tmp.append(cur.value)
        if cur.left:
            ele_list.put(cur.left)
            n_last = cur.left

        if cur.right:
            ele_list.put(cur.right)
            n_last = cur.right

        if last == cur:
            last = n_last
            res.append(tmp)
            tmp = []

    return res


a = Tree()
b = Tree()
c = Tree()
d = Tree()
e = Tree()
f = Tree()


a.value = 1
a.left = b
a.right = c

b.value = 2
b.left = d
b.right = e

c.value = 3
c.left = f

d.value = 4
e.value = 5
f.value = 6

print(getArray(a))


q = Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())

arr = [1,2,3]
print(arr.pop(0))

set_1 = set()
set_1.add(1)
set_1.add(2)
set_1.add(3)
print(set_1.pop())




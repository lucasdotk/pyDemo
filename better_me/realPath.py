#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/6 11:51 上午 
# @Author  : kuangchao@zingfront.com
# @File    : realPath.py
# @Description :


def get_real_path(path):
    elem_list = path.split('/')
    stack = []
    for e in elem_list:
        if e == '..' and len(stack) > 0:
            stack.pop()
        elif e not in ['', '.', '..']:
            stack.append(e)

    return '/' + '/'.join(stack)


p = '/../'
print(get_real_path(p))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/12/29 4:24 下午 
# @Author  : kuangchao@zingfront.com
# @File    : demo2.py
# @Description :


import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://httpbin.org/headers')
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

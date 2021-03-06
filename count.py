#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/4/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃   ┻    ┃
            ┗━┓    ┏━┛
              ┃    ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃  永无BUG！ ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛

when I wrote this,only God and I understood what I was doing.
Now,God only knows.

"""

"""
    毕设结果分析
    根据effect size的正负，统计正负调控
"""

import sys
from itertools import islice

"""
    islice(iterable, stop) --> islice object
    islice(iterable, start, stop[, step]) --> islice object
"""

def func(filename):

    #不能用result=[[0,0]]*10,否则所有单个元素都会更新
    result=[0,0]
    fileder=open(filename)

    for line in islice(fileder,1,None):
        lines=line.strip().split('\t')#strip()用来去除换行符
        if lines[4].startswith('-'):
            result[1]+=1
        else:
            result[0]+=1

    return result

if __name__ == '__main__':
    filename=sys.argv[1]

    result=func(filename)
    print(result)

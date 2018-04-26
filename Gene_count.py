#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/4/26'
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
    统计哪些基因区域出现了不止一个位点

"""

import sys

def func(filename):
    fileder=open(filename)
    count=0
    result={}
    line_num=0
    for line in fileder:
        line_num+=1
        lines=line.split('\t')
        if lines[0] in result:
            result[lines[0]]+=1
        else:
            result[lines[0]]=1

    print(line_num)
    #print(result)
    for key in result.keys():
        if result[key]>1:
            count+=1
        else:
            continue

    fileder.close()
    return count

if __name__ == '__main__':
    filename=sys.argv[1]
    result=func(filename)
    print(result)
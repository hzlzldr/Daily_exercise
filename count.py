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

fileder1=open("a_count")
fileder2=open("b_count")

#不能用result_a=[[0,0]]*10,否则所有单个元素都会更新
result_a=[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
result_b=[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


for line in fileder1:
    lines=line.strip().split('\t')#strip()用来去除换行符
    if len(lines)!=10:#数据集有行数只有9个元素，需要单独处理
        continue
    else:
        for i in range(10):
            if lines[i].startswith("-"):#这个数据集有问题，内容是字符串，无法用float转换成numeric，奇淫技巧
                result_a[i][0]+=1
            else:
                result_a[i][1]+=1


for line in fileder2:
    lines=line.strip().split('\t')#strip()用来去除换行符
    if len(lines)!=10:#数据集有行数只有9个元素，需要单独处理
        continue
    else:
        for i in range(10):
            if lines[i].startswith("-"):#这个数据集有问题，内容是字符串，无法用float转换成numeric，奇淫技巧
                result_b[i][0]+=1
            else:
                result_b[i][1]+=1

fileder1.close()
fileder2.close()

print(result_a)
print(result_b)


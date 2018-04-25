#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/4/25'
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

蒙特卡罗方法（英语：Monte Carlo method），也称统计模拟方法，是1940年代中期由于科学技术的发展和电子计算机的发明，
而提出的一种以概率统计理论为指导的数值计算方法。是指使用随机数（或更常见的伪随机数）来解决很多计算问题的方法。

思想：假想你有一袋豆子，把豆子均匀地朝这个图形上撒，然后数这个图形之中有多少颗豆子，这个豆子的数目就是图形的面积。
当你的豆子越小，撒的越多的时候，结果就越精确。借助计算机程序可以生成大量均匀分布坐标点，然后统计出图形内的点数，通过它们占总点数的比例和坐标点生成范围的面积就可以求出图形面积。

"""

import time
import random

def func1(duplication_num=1000000):
    """
    (π*r^2)/2*2=p,r=1,p为落入圆内的概率
    to calculate π
    :return: approximate π
    """

    count = 0
    for _ in range(duplication_num):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)

        if pow(x,2)+pow(y,2)<=1:
            count+=1
        else:
            continue

    return float(4*count/duplication_num)

def func2(duplication_num=1000000):
    """
    to calculate the integration of f(x)=x^2 in x∈[0,1]
    :return:the result of integration
    """
    count=0
    for _ in range(duplication_num):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if y<=pow(x,2):
            count+=1
        else:
            continue

    return float(count/duplication_num)

if __name__ == '__main__':
    pai=func1()
    integration=func2()
    print(pai)
    print(integration)
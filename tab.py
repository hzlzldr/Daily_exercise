#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/5/8'
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

import sys

"""
    用于判断GWAS位点与基因和1M之间的关系
"""

def func(filename):
    fileder=open(filename)
    name="2_gene.bed"
    file=open(name,'w')
    result={}
    for line in fileder:
        lines=line.strip().split('\t')
        if int(lines[-1])<1000000:
            result[lines[3]]=1
        else:
            continue
        #print(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5])
        # lines=line.strip().split('\t')
        # try:
        #     lines_1=lines[0].strip().split(' ')
        #     lines_2=lines[1].strip().split(' ')
        #     file.write("{0}\t{1}\t{2}\t{3}\t{4}\t\n".format(lines_1[0], lines_1[1], lines_1[2], lines_2[1], int(1)))
        # #print(lines_1[0],lines_1[1],lines_1[2],lines_2[1])
        # except:
        #     pass
        #file.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(lines[0]
         #           ,lines[1],lines[2],lines[4],1,lines[5]))
    print(len(result.keys()))
    file.close()
    fileder.close()


if __name__ == '__main__':
    filename=sys.argv[1]
    func(filename)
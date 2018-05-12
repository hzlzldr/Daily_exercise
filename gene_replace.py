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

def replace(map_filename,ref_filename,ret_filename="ret_replace.txt"):
    fileder1=open(map_filename)
    fileder2=open(ref_filenmae)

    file=open(ret_filename,'w+')

    map_lst={}
    for line in fileder1:
        lines=line.strip().split('\t')
        version=eval(lines[9]).split('.')
        map_lst[version[0]]=lines


    ref_lst={}
    for line in fileder2:
        lines=line.strip().split('\t')
        if len(lines)==4:
            continue
        else:
            ref_lst[lines[-1]]=lines

    for index in map_lst:
        if index in ref_lst.keys():
            map_lst[index].append(ref_lst[index][2])
            map_lst[index].append(ref_lst[index][3])
            file.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t"
                       "{12}\t{13}\t{14}\n".format(map_lst[index][0],map_lst[index][1],
                        map_lst[index][2],map_lst[index][3],map_lst[index][4],map_lst[index][5],
                        map_lst[index][6],map_lst[index][7],map_lst[index][8],map_lst[index][9],
                        map_lst[index][10],map_lst[index][11],map_lst[index][12],
                                                   map_lst[index][13],map_lst[index][14]))

    file.close()
    fileder2.close()
    fileder1.close()

if __name__ == '__main__':
    try:
        map_filename=sys.argv[1]
        ref_filenmae=sys.argv[2]
        ret_filename=sys.argv[3]
        replace(map_filename,ref_filenmae,ret_filename)
    except:
        map_filename = sys.argv[1]
        ref_filenmae = sys.argv[2]
        replace(map_filename, ref_filenmae)
    finally:
        print("hello world")

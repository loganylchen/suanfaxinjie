#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 下午12:59
# @Author  : Chen Yuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : commons.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os, sys
from functools import wraps
import time
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def how_long(func):
    '''
    这是一个装饰器
    :param func:
    :return:
    '''

    @wraps(func)
    def print_time(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        print('{func_name}() cost:{ms} ms!'.
              format(func_name=func.__name__,
                     ms='%.4f' % ((end - start) * 1000)))
        return result
    return print_time

@how_long
def what(somenumber):
    '''

    :param someword:
    :return:
    '''
    sum=0
    for i in range(somenumber):
        sum+=i
    return sum

def main():
    # what(1000)
    # what(100000000)
    a=[False]*3
    print(a)


if __name__ == '__main__':
    main()
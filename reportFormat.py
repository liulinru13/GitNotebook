#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def exec(cmd):
  result_code = os.system(cmd)
  if result_code != 0:
    log("命令执行失败 ===> " + cmd)
    exit(1)

'''
从命令行读取数据
'''
def popen(cmd):
  stream = os.popen(cmd)
  result = stream.read().rstrip()
  stream.close()
  return result
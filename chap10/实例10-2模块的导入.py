'''
import 模块名 【as 别名】
from 模块名 import 函数/类/属性/*
'''
#(1)
import numpy as n
import my_info
my_info.info()
import my_info as a
print(a.name)
print(a.info())
#(2)
from my_info import name
print(name)
# info()
from my_info import info
info()
#通配符*
from my_info import *
print(name)
info()
#同时导入多个模块，用，分隔
import math,time,random,os
#coding=utf-8
#倒入模块的几种方式
"""
import functions
functions.print_models('tomato','potato','banana')
"""
"""
import functions as func
func.print_models('tomato','potato','banana')
"""
"""
from functions import print_models
print_models('tomato','potato','banana')
"""
"""
from functions import *
print_models('tomato','potato','banana')
"""
from functions import print_models as pm
pm('tomato','potato','banana')

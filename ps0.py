#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:21:43 2021

@author: wooyoung
"""

import math
import numpy as np
import matplotlib

x = int(input("Enter number x:"))
y = int(input("Enter number y:"))
print("X**y =",  x**y)
print("log(x) =", int(math.log2(x)))


exp = x ** y
log = math.log2(x)
print("X**y = %d" % exp)
print("log(x) = %d" %log)

#!/usr/bin/env python
#coding=utf-8
import matplotlib.pyplot as plt 
from random_walk import RandomWalk
rw=RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
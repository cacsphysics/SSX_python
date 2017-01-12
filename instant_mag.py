#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:25:42 2017

@author: ccartagena
"""

import pickle
import numpy as np
import scipy.optimize as optimization
#import math as m
#import matplotlib.pylab as plt


with open('mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
    
instant_magn = np.zeros(20)

for i in range(0,20):
    instant_magn[i] = b[1,i,0]

position = np.zeros(20)

for i in range(0,20):
    position[i] = i*1.5

mag_uncertainty = instant_magn * 0.1
xo = np.array([ 0.03212442, 0.00459985, -0.00703278])

def func(x,a,b,c):
    return a * np.sin(b*x + c)

print optimization.curve_fit(func, position, instant_magn,xo, mag_uncertainty)
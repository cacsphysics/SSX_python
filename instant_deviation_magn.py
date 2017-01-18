#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:21:35 2017
 This script is to be used to determine the limit of averaging
@author: ccartagena
"""

import pickle
import numpy as np
#import scipy.optimize as optimization
#import math as m
import matplotlib.pylab as plt

#--------------------------------------
# Loading the structured data
#--------------------------------------
with open('mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
#--------------------------------------

#--------------------------------------
# The point of this chunk of code is to gain
# a perspective of the time interval for averaging.
# ~10
#--------------------------------------
def timePerspective(div):    
    d = 0.0
    i = 1400
    while (d < div):
    
        for j in range(0,19):
            if d < b[0,j,1400] - b[0,j,i + 1]:
                d = b[0,j,1400] - b[0,j,i + 1]
                pos = j
        i = i + 1
    return d, pos, i
#--------------------------------------

#--------------------------------------
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep).
#--------------------------------------
def magneticTimeAvg(istep,fstep):
    bAvg = np.zeros(19)
    for i in range(0,19):
        for j in range(istep,fstep):
            bAvg[i] = bAvg[i] + b[0,i,j]/10.0
    return bAvg
#--------------------------------------
position = np.arange(19)*1.5
plt.figure(1)
plt.clf()
plt.plot(position,bAvg,'o',linestyle = 'dotted' )
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')
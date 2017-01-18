#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:25:42 2017
Plotting the instanteous magnetic field
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
# Defining position array in cm
#--------------------------------------
position = np.arange(19) * 1.5
#--------------------------------------

plt.figure(1)
plt.clf()
plt.plot(position,b[0,0:19,1400],'o',linestyle = 'dotted' )
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')

plt.figure(2)
plt.clf()
plt.plot(position,b[0,0:19,1401],'o',linestyle = 'dotted' )
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')

plt.figure(3)
plt.clf()
plt.plot(position,b[0,0:19,1402],'o',linestyle = 'dotted' )
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')
"""
This was the curve fit attempt 

#mag_uncertainty = instant_magn * 0.1
#xo = np.array([ 0.67609157, 2.50541118, -0.56249263])

#def func(x,a,b,c):
#    return a * np.sin(b*x + c)

#print optimization.curve_fit(func, position, instant_magn,xo, mag_uncertainty)
"""
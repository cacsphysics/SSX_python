#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:21:35 2017
 This script is to be used to determine the limit of averaging
@author: ccartagena
"""

import pickle
import numpy as np
import scipy.optimize as optimization
import math as m
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
    i = 1909
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
# final time step(fstep). x direction
#--------------------------------------
def xmagneticTimeAvg(istep,fstep):
    xbAvg = np.zeros(20)
    for i in range(0,20):
        for j in range(istep,fstep):
            xbAvg[i] = xbAvg[i] + b[0,i,j]/(fstep - istep + 1)
    return xbAvg
#--------------------------------------

#--------------------------------------
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep). y direction
#--------------------------------------
def ymagneticTimeAvg(istep,fstep):
    ybAvg = np.zeros(20)
    for i in range(0,20):
        for j in range(istep,fstep):
            ybAvg[i] = ybAvg[i] + b[1,i,j]/(fstep - istep + 1)
    return ybAvg
#--------------------------------------

#--------------------------------------
# the plotting of a set of data
#--------------------------------------
def sine_plot(pos,bAvg,title):
    plt.figure()
    plt.clf()
    plt.plot(pos,bAvg,'o',linestyle = 'dotted' )
    #plt.plot(position,bAvg,'o')
    plt.xlabel('Position [cm]')
    plt.ylabel('B [G]')
    plt.ylim(-600,600)
    plt.title(title)
    savefile = 'mjmag_' + title + '.png'
    plt.savefig(savefile, dpi = 100, facecolor = 'w', edgecolor = 'k')
    plt.close()
#--------------------------------------

#--------------------------------------
# This function produces the figures for the  averages over
# 100 steps. 
#--------------------------------------
def plot_100avg_xpos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = xmagneticTimeAvg(istep, istep + 100)
        title = 'x_' + str(istep) + '-' + str(istep + 100)
        sine_plot(pos,bAvg,title)
        istep = istep + 100
#--------------------------------------

#--------------------------------------
# This function produces the figures for the averages over
# 50 steps.
#--------------------------------------
def plot_50avg_xpos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = xmagneticTimeAvg(istep, istep + 50)
        title = 'x_' + str(istep) + '-' + str(istep + 50)
        sine_plot(pos,bAvg,title)
        istep = istep + 50
#--------------------------------------

#--------------------------------------
# This function produces the figures for the  averages over
# 100 steps. 
#--------------------------------------
def plot_100avg_ypos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = ymagneticTimeAvg(istep, istep + 100)
        title = 'y_' + str(istep) + '-' + str(istep + 100)
        sine_plot(pos,bAvg,title)
        istep = istep + 100
#--------------------------------------

#--------------------------------------
# This function produces the figures for the averages over
# 50 steps.
#--------------------------------------
def plot_50avg_ypos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = ymagneticTimeAvg(istep, istep + 50)
        title = 'y_' + str(istep) + '-' + str(istep + 50)
        sine_plot(pos,bAvg,title)
        istep = istep + 50
#--------------------------------------
"""
#--------------------------------------
# This function produces the figures for the averages over
# 80 steps.
#--------------------------------------
def plot_80avg_xpos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = magneticTimeAvg(istep, istep + 80)
        title = str(istep) + '-' + str(istep + 80)
        sine_plot(pos,bAvg,title)
        istep = istep + 80
#--------------------------------------
"""
"""
#--------------------------------------
# Defining the time averaged magnetic field
# and position vectors
#--------------------------------------
bAvg = magneticTimeAvg(2500,2600)
position = np.arange(20)*1.5
#--------------------------------------


#--------------------------------------
# Plotting to obtain a visual of the data
#--------------------------------------
plt.figure(1)
plt.clf()
plt.plot(position,bAvg,'o',linestyle = 'dotted' )
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')
#--------------------------------------
"""
#--------------------------------------
# Running the curve fit
#--------------------------------------
#--------------------------------------
# Setting inital values
#--------------------------------------
"""magWeight = np.zeros(20)
for i in range(1,21):
    magWeight[-i] = (i+1)

#magWeight = bAvg*0.1
#magWeight = np.array([1,1,2,1,1,1,6,10,6,10,10,6,6,10,6,6,6,10,6,6])        

xo = np.array([50.0, 2*m.pi/3.5, 0.0,0.0])
bou = [(10.0, 0, -m.pi,-10.0), (150.0, 4*m.pi, m.pi, 10.0)]
#--------------------------------------
def func(x,a,b,c,d):
    return a * np.sin(b*x + c) + d

print optimization.curve_fit(func, position, bAvg, p0 = xo, 
                             sigma = magWeight, bounds = bou)
#--------------------------------------
"""



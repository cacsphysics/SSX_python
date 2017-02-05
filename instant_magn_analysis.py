#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:21:35 2017
 This is the beginning of a library focusing on analysis
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
def sine_plot(pos, bAvg, title):
    plt.figure()
    plt.clf()
    plt.plot(pos,bAvg,'o',linestyle = 'dotted' )
    #plt.plot(position,bAvg,'o')
    plt.xlabel('Position [cm]')
    plt.ylabel('B [G]')
    plt.ylim(-600,600)
    plt.title(title)
    savefile = 'mjmag_' + title + '.png'
    plt.savefig(savefile, facecolor = 'w', edgecolor = 'k')
    plt.close()
#--------------------------------------

#--------------------------------------
# the plotting of a set of x and y data
#--------------------------------------
def sine_plot(pos, xbAvg, ybAvg, title):
    
    fig = plt.figure(num = 2)
    
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    
    #fig.suptitle(title)
    
    ax1.axis([0,20*1.5,-600,600])
    ax2.axis([0,20*1.5,-600,600])
    
    ax1.minorticks_on()
    ax2.minorticks_on()
    
    for tick in ax1.xaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = False
    
    ax1.set_ylabel('B [G]')
    ax2.set_ylabel('B [G]')
    ax2.set_xlabel('Position [cm]')
    
    fig.text(0.45,0.5, title)
    ax1.text(0.05,0.8, r'(x)', transform = ax1.transAxes)
    ax2.text(0.05,0.8, r'(y)', transform = ax2.transAxes)
    
    
    ax1.plot(pos, xbAvg, 'ro', linestyle = 'dotted')
    ax2.plot(pos, ybAvg, 'bo', linestyle = 'dotted')
    
    savefile = 'mjmag_' + title + '.png'
    fig.savefig(savefile)
    plt.close(fig)
#--------------------------------------

#--------------------------------------
# This function produces the figures for the  averages over
# 100 steps. 
#--------------------------------------
def plot_100avg_xpos_mag(istep, fstep):
    
    pos = np.arange(20) * 1.5
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
    
    pos = np.arange(20) * 1.5
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
    
    pos = np.arange(20) * 1.5
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
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        bAvg = ymagneticTimeAvg(istep, istep + 50)
        title = 'y_' + str(istep) + '-' + str(istep + 50)
        sine_plot(pos,bAvg,title)
        istep = istep + 50
#--------------------------------------

#--------------------------------------
# This function produces the figures for the 
# averages over 100 of x and y 
#--------------------------------------
def plot_100avg_xypos_mag(istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        xbAvg = xmagneticTimeAvg(istep, istep + 100)
        ybAvg = ymagneticTimeAvg(istep, istep + 100)
        title =  str(round(timeb[istep],1)) + '-' + str(round(timeb[istep + 100],1))+ 'us'
        sine_plot(pos, xbAvg, ybAvg, title)
        istep = istep + 100
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
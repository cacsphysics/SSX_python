#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:46:51 2017

@author: ccartagena
"""
import pickle
import numpy as np
import scipy.optimize as optimization
import math as m
import matplotlib.pylab as plt
import instant_magn_analysis as inmag




#--------------------------------------
# Loading the structured data
#--------------------------------------
with open('Pickle_files/mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
#--------------------------------------

#--------------------------------------
"""
Plotting procedure
"""
#--------------------------------------
def sine_data1x(bAvg, pos, amp, waveNum, phase, title):
    
    
    # Set fitted curve
    distance = np.zeros(1000)
    
    for i in range(0,1000):
        distance[i] = pos[0] + (pos[-1]- pos[0])/1000.0 * i
            
    sine_data = amp * np.sin((waveNum * distance +  phase))
                              
    # Make a figure
    fig = plt.figure(num = 1)
    fig.canvas.set_window_title('mjxmag_' + title + '_fit')
    ax = fig.add_subplot(1,1,1)
    
    # Set axis ranges
    ax.axis([pos[0], pos[-1], -600, 600])
    ax.minorticks_on()
    
    # Label axis
    ax.set_xlabel(r'Position [cm]')
    ax.set_ylabel(r'B [G]')
   
    ax.text(0.05,0.95, title, transform = ax.transAxes)
    ax.text(0.05,0.9, "wavelength = " +  str(2*m.pi/waveNum),
            transform = ax.transAxes)
    
    # Plotting data and fit
    ax.plot(pos, bAvg, 'o', linestyle = 'dotted')
    ax.plot(distance, sine_data)
    
    
    plt.show(fig)
    plt.close(fig)


#--------------------------------------

#--------------------------------------
"""
Plotting procedure
"""
#--------------------------------------
def sine_data1y(bAvg, pos, amp, waveNum, phase, title):
    
    
    # Set fitted curve
    distance = np.zeros(1000)
    
    for i in range(0,1000):
        distance[i] = pos[0] + (pos[-1]- pos[0])/1000.0 * i
            
    sine_data = amp * np.sin((waveNum * distance +  phase))
                              
    # Make a figure
    fig = plt.figure(num = 1)
    fig.canvas.set_window_title('mjymag_' + title + '_fit')
    ax = fig.add_subplot(1,1,1)
    
    # Set axis ranges
    ax.axis([pos[0], pos[-1], -600, 600])
    ax.minorticks_on()
    
    # Label axis
    ax.set_xlabel(r'Position [cm]')
    ax.set_ylabel(r'B [G]')
   
    ax.text(0.05,0.95, title, transform = ax.transAxes)
    ax.text(0.05,0.9, "wavelength = " +  str(2*m.pi/waveNum),
            transform = ax.transAxes)
    
    # Plotting data and fit
    ax.plot(pos, bAvg, 'o', linestyle = 'dotted')
    ax.plot(distance, sine_data)
    
    
    plt.show(fig)
    plt.close(fig)


#--------------------------------------

#--------------------------------------
"""
Plotting procedure
"""
#--------------------------------------
def sine_data2x(bAvg, pos, amp, waveNum, phase, shift, title):
    
    
    # Set fitted curve
    distance = np.zeros(1000)
    
    for i in range(0,1000):
        distance[i] = pos[0] + (pos[-1]- pos[0])/1000.0 * i
            
    sine_data = amp * np.sin(waveNum * distance +  phase) + shift
                              
    # Make a figure
    fig = plt.figure(num = 1)
    fig.canvas.set_window_title('mjxmag_' + title + 'us_fit')
    ax = fig.add_subplot(1,1,1)
    
    # Set axis ranges
    ax.axis([pos[0], pos[-1], -600, 600])
    ax.minorticks_on()
    
    # Label axis
    ax.set_xlabel(r'Position [cm]')
    ax.set_ylabel(r'B [G]')
    
    ax.text(0.05,0.95, title, transform = ax.transAxes)
    ax.text(0.05,0.9, "wavelength = " +  str(2*m.pi/waveNum),
            transform = ax.transAxes)
    
    # Plotting data and fit
    ax.plot(pos, bAvg, 'o', linestyle = 'dotted')
    ax.plot(distance, sine_data)
    
    
    plt.show(fig)
    plt.close(fig)


#--------------------------------------

#--------------------------------------
"""
Plotting procedure
"""
#--------------------------------------
def sine_data2y(bAvg, pos, amp, waveNum, phase, shift, title):
    
    
    # Set fitted curve
    distance = np.zeros(1000)
    
    for i in range(0,1000):
        distance[i] = pos[0] + (pos[-1]- pos[0])/1000.0 * i
            
    sine_data = amp * np.sin(waveNum * distance +  phase) + shift
                              
    # Make a figure
    fig = plt.figure(num = 1)
    fig.canvas.set_window_title('mjymag_' + title + 'us_fit')
    ax = fig.add_subplot(1,1,1)
    
    # Set axis ranges
    ax.axis([pos[0], pos[-1], -600, 600])
    ax.minorticks_on()
    
    # Label axis
    ax.set_xlabel(r'Position [cm]')
    ax.set_ylabel(r'B [G]')
    
    ax.text(0.05,0.95, title, transform = ax.transAxes)
    ax.text(0.05,0.9, "wavelength = " +  str(2*m.pi/waveNum),
            transform = ax.transAxes)
    
    # Plotting data and fit
    ax.plot(pos, bAvg, 'o', linestyle = 'dotted')
    ax.plot(distance, sine_data)
    
    
    plt.show(fig)
    plt.close(fig)


#--------------------------------------

#--------------------------------------
"""
 This function takes the averages of the time interval 
 fstep - istep and defines the spacial interval which 
 to apply the curve fit, fpoint - epoint.
"""
#--------------------------------------
def data_interval_x(istep, fstep, spoint, epoint):
    
    bAvg = inmag.xmagneticTimeAvg(istep,fstep)
    pos = np.arange(20)*1.5
    title =  str(round(timeb[istep],1)) + '-' + str(round(timeb[fstep],1))+ 'us'
    
    bAvgInterval = bAvg[spoint:epoint]
    posInterval = pos[spoint:epoint]
    
    return bAvgInterval, posInterval, title

def data_interval_y(istep, fstep, spoint, epoint):
    
    bAvg = inmag.ymagneticTimeAvg(istep,fstep)
    pos = np.arange(20)*1.5
    title =  str(round(timeb[istep],1)) + '-' + str(round(timeb[fstep],1))+ 'us'
    
    bAvgInterval = bAvg[spoint:epoint]
    posInterval = pos[spoint:epoint]
    
    return bAvgInterval, posInterval, title

#--------------------------------------
# Running the curve fit
#--------------------------------------
#--------------------------------------
# Setting inital guesses and values
#--------------------------------------

"""
#magWeight = bAvg*0.1
#magWeight = np.array([1,1,2,1,1,1,6,10,6,10,10,6,6,10,6,6,6,10,6,6])        
"""
bAvg, pos, title = data_interval_y(2300,2400,7,16)

"""
magWeight = np.zeros(pos.size)
for i in range(1,pos.size + 1):
    magWeight[-i] = (i+1)
"""
#--------------------------------------
# xo correspons to the intial guesses.
# Note: The number of elements depend on the function used.
#--------------------------------------
#xo = np.array([300.0, 2*m.pi/3.5, 0.0,0.0])
xo = np.array([200.0, 2*m.pi/0.95 , 0.0])
#--------------------------------------

#--------------------------------------
# bou is a restriction on the possible outputs of each variable
# from the curve_fit.

# [lower restriction, upper restriction]

#--------------------------------------
#bou = [(10.0, 0, -m.pi,-10.0), (150.0, 4*m.pi, m.pi, 10.0)]
bou = [(100.0, 0, -m.pi), (600.0, 4*m.pi, m.pi)]
#--------------------------------------

#--------------------------------------
"""
 The possible functions for the curve fit.
"""
#--------------------------------------

def func1(x,a,b,c):
    return a * np.sin(b * x + c)

def func2(x,a,b,c,d):
    return a * np.sin(b * x + c) + d
#--------------------------------------


#vari,comat = optimization.curve_fit(func1, pos, bAvg, p0 = xo,
#                                 bounds = bou, sigma = magWeight)

vari,comat = optimization.curve_fit(func1, pos, bAvg, p0 = xo,
                                 bounds = bou)

print vari, comat

sine_data1y(bAvg, pos, vari[0], vari[1], vari[2], title)

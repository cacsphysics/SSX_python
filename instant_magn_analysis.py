 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:21:35 2017
 This is the beginning of a library focusing on analysis
@author: ccartagena
"""

import pickle
import numpy as np
#import scipy.optimize as optimization
#import math as m
import process_mjmag_data as mj
import matplotlib.pylab as plt

"""
################### All Functions ########################
# Depend on the variables time, bdot, timeb , b and bmod #
##########################################################

 They are defined by using the mjmag_load function:
 
 time,bdot,timeb,b,bmod = mjmag_load(date, shot)
 
"""
"""
#--------------------------------------
# Loading the structured data
#--------------------------------------
with open('/Users/ccartagena/Carlos/Pickle_files/mag' 
          + date + '_'+  shot +'_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
#--------------------------------------

#--------------------------------------
# The function saves the processes the data and saves 
# it as a pickle file. 
#--------------------------------------
"""
"""
The data parameter must be a string corresponding to the month_day_year 
without any delimiters, i.e. date = 123016 - 12/30/16

The shot parameter is an integer which corresponds to the shot number.

date = '123016'
shot = 92;
def mjmag_sav(date, shot):
    
    time,bdot,timeb,b,bmod,fulldata = mj.process_mjmag_data(date+str(shot))
    
    with open('/Users/ccartagena/Carlos/Pickle_files/mag' + date + '_'
            + str(shot) + '_data.pickle','w') as f:
        pickle.dump([time,bdot,timeb,b,bmod],f)
#--------------------------------------

#--------------------------------------
# Loading the structured data
#--------------------------------------


The data parameter must be a string corresponding to the month_day_year 
without any delimiters, i.e. date = 123016 - 12/30/16

The shot parameter is an integer which corresponds to the shot number.


def mjmag_load(date, shot):
    
    with open('/Users/ccartagena/Carlos/Pickle_files/mag' 
              + date + '_'+  str(shot) +'_data.pickle') as f:
       time,bdot,timeb,b,bmod = pickle.load(f)
    return time, bdot, timeb, b, bmod
#--------------------------------------
"""
"""
This function is not helpful. I am debating about deleting it.
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
"""
#--------------------------------------
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep). x direction
#--------------------------------------
def xmagneticTimeAvg(b,istep, fstep):
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
def ymagneticTimeAvg(b, istep, fstep):
    ybAvg = np.zeros(20)
    for i in range(0,20):
        for j in range(istep,fstep):
            ybAvg[i] = ybAvg[i] + b[1,i,j]/(fstep - istep + 1)
    return ybAvg
#--------------------------------------

#--------------------------------------
# the plotting of a set of data
#--------------------------------------
def sine_plot1(pos, bAvg, title):
    plt.figure()
    plt.clf()
    plt.plot(pos,bAvg,'o',linestyle = 'dotted' )
    #plt.plot(position,bAvg,'o')
    plt.xlabel('Position [cm]')
    plt.ylabel('B [G]')
    plt.ylim(-600,600)
    plt.title(title)
    savefile = 'mjmag_' + date + '_' + str(shot) + '_' + title + '.png'
    plt.savefig(savefile, facecolor = 'w', edgecolor = 'k')
    plt.close()
#--------------------------------------

#--------------------------------------
# the plotting of a set of x and y data
#--------------------------------------
def sine_plot2(date, shot, pos, xbAvg, ybAvg, title):
    
    # Overall Figure with two subplots
    fig = plt.figure(num = 2)
    
    # Setting the two subplots
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    
    #fig.suptitle(title)
    
    # Setting the axes
    ax1.axis([-3,20*1.5,-600,600])
    ax2.axis([-3,20*1.5,-600,600])
    
    ax1.minorticks_on()
    ax2.minorticks_on()
    
    for tick in ax1.xaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = False
    
    ax1.set_ylabel('B [G]')
    ax2.set_ylabel('B [G]')
    ax2.set_xlabel('Position [cm]')
        # Indicator Vertical Lines
    ax1.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
    ax1.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
    ax1.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
    ax2.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
    ax2.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
    ax2.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)
    
    
    # Setting Figure title
    fig.text(0.4667,0.925,date + 'r' + str(shot),size = 18)
    
    # Setting Figure text
    fig.text(0.775,0.49, 'Beginning of FC', color = 'grey')
    fig.text(0.125,0.49, 'End of FC', color = 'grey')
    fig.text(0.5,0.49, 'Triplet IDS/HeNe')
    fig.text(0.8,0.925, title)
    ax1.text(0.015,0.875, r'(x)', transform = ax1.transAxes)
    ax2.text(0.015,0.875, r'(y)', transform = ax2.transAxes)

    # Plotting the data
    ax1.plot(pos, xbAvg, 'ro', linestyle = 'dotted')
    ax2.plot(pos, ybAvg, 'bo', linestyle = 'dotted')
    
    # Saving the overall figure
    savefile = 'mjmag_' + date + '_' + str(shot) + '_' + title + '.png'
    fig.savefig(savefile)
    plt.close(fig)
#--------------------------------------

#--------------------------------------
# This function is ment to plot 4 sin_plot2 plots
#--------------------------------------
def four_plot(pos, xbAvg, ybAvg, title):
    
    # Overall Figure with two subplots
    fig = plt.figure(num = 2)
    
    # Setting the two subplots
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    
    #fig.suptitle(title)
    
    # Setting the axes
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
    """
        # Indicator Vertical Lines
    ax1.axvline(x = 1.5, linestyle = 'solid', color = 'purple', linewidth = 2)
    ax1.axvline(x = 18, linestyle = 'solid', color = 'black', linewidth = 2)
    ax1.axvline(x = 28.5, linestyle = 'solid', color = 'purple', linewidth = 2)    
    ax2.axvline(x = 1.5, linestyle = 'solid', color = 'purple', linewidth = 2)
    ax2.axvline(x = 18, linestyle = 'solid', color = 'black', linewidth = 2)
    ax2.axvline(x = 28.5, linestyle = 'solid', color = 'purple', linewidth = 2)
    
    
    # Setting Figure title
    fig.text(0.4667,0.925,date + 'r' + str(shot),size = 18)
    
    # Setting Figure text
    fig.text(0.775,0.49, 'Beginning of FC', color = 'purple')
    fig.text(0.125,0.49, 'End of FC', color = 'purple')
    fig.text(0.5,0.49, 'Triplet IDS/HeNe')
    fig.text(0.8,0.925, title)
    ax1.text(0.015,0.875, r'(x)', transform = ax1.transAxes)
    ax2.text(0.015,0.875, r'(y)', transform = ax2.transAxes)
    """
    # Plotting the data
    ax1.plot(pos, xbAvg, 'ro', linestyle = 'dotted')
    ax2.plot(pos, ybAvg, 'bo', linestyle = 'dotted')
    
    # Saving the overall figure
    savefile = 'mjmag_' + date + '_' + str(shot) + '_' + title + '.png'
    fig.savefig(savefile)
    plt.close(fig)
#--------------------------------------

#--------------------------------------
# This function produces the figures for the  averages over
# 100 steps. 
#--------------------------------------
def plot_100avg_xpos_mag(b, timeb, istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        bAvg = xmagneticTimeAvg(b, istep, istep + 100)
        title = 'x_' + str(istep) + '-' + str(istep + 100)
        sine_plot1(pos,bAvg,title)
        istep = istep + 100
#--------------------------------------

#--------------------------------------
# This function produces the figures for the averages over
# 50 steps.
#--------------------------------------
def plot_50avg_xpos_mag(b, timeb, istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        bAvg = xmagneticTimeAvg(b, istep, istep + 50)
        title = 'x_' + str(istep) + '-' + str(istep + 50)
        sine_plot1(pos,bAvg,title)
        istep = istep + 50
#--------------------------------------

#--------------------------------------
# This function produces the figures for the  averages over
# 100 steps. 
#--------------------------------------
def plot_100avg_ypos_mag(b, timeb, istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        bAvg = ymagneticTimeAvg(b, istep, istep + 100)
        title = 'y_' + str(istep) + '-' + str(istep + 100)
        sine_plot1(pos,bAvg,title)
        istep = istep + 100
#--------------------------------------

#--------------------------------------
# This function produces the figures for the averages over
# 50 steps.
#--------------------------------------
def plot_50avg_ypos_mag(b, timeb, istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        bAvg = ymagneticTimeAvg(b, istep, istep + 50)
        title = 'y_' + str(istep) + '-' + str(istep + 50)
        sine_plot1(pos,bAvg,title)
        istep = istep + 50
#--------------------------------------

#--------------------------------------
# This function produces the figures for the 
# averages over 100 of x and y 
#--------------------------------------
def plot_100avg_xypos_mag(b, timeb, istep, fstep):
    
    pos = np.arange(20) * 1.5
    while(istep < fstep):
        xbAvg = xmagneticTimeAvg(b, istep, istep + 100)
        ybAvg = ymagneticTimeAvg(b, istep, istep + 100)
        title =  str(round(timeb[istep],1)) + '-' + str(round(timeb[istep + 100],1))+ 'us'
        sine_plot2(pos, xbAvg, ybAvg, title)
        istep = istep + 100
#--------------------------------------

#--------------------------------------
# This function produces the figures for the
# averages over 25 of x and y
#--------------------------------------
def plot_25avg_xypos_mag(date, shot, b, timeb, istep, fstep):
    

    pos = np.arange(20)*1.5 - 2.86
        
    while(istep < fstep):
        xbAvg = xmagneticTimeAvg(b, istep, istep + 25)
        ybAvg = ymagneticTimeAvg(b, istep, istep + 25)
        title =  str(round(timeb[istep],1)) + '-' + str(round(timeb[istep + 25],1))+ 'us'
        sine_plot2(date, shot, pos, xbAvg, ybAvg, title)
        istep = istep + 25
#--------------------------------------
"""
80 steps is a random number with no significance.
#--------------------------------------
# This function produces the figures for the averages over
# 80 steps.
#--------------------------------------
def plot_80avg_xpos_mag(istep, fstep):
    
    pos = np.arange(20)*1.5
    while(istep < fstep):
        bAvg = magneticTimeAvg(istep, istep + 80)
        title = str(istep) + '-' + str(istep + 80)
        sine_plot1(pos,bAvg,title)
        istep = istep + 80
#--------------------------------------
"""
def work_in_progress():
    
    L = [[2000,2100], [2100,2200], [2200,2300], [2300,2400]]

    xMag = []
    yMag = []
    
    for i in range(4):
        
        x = xmagneticTimeAvg(L[i][0], L[i][1])
        y = ymagneticTimeAvg(L[i][0], L[i][1])
        
        xMag.append(x)
        yMag.append(y)
    

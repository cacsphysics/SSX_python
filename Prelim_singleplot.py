#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:22:10 2017

@author: ccartagena
"""

import pickle
import numpy as np
import matplotlib.pylab as plt

#--------------------------------------
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep). x direction
#--------------------------------------
def xmagneticTimeAvg(b, istep, fstep):
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
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep). mod direction
#--------------------------------------
def modmagneticTimeAvg(istep, fstep):
    bmodAvg = np.zeros(20)
    for i in range(0,20):
        for j in range(istep,fstep):
            bmodAvg[i] = bmodAvg[i] + bmod[i,j]/(fstep - istep + 1)
    return bmodAvg
#--------------------------------------
"""
This is where you need to make changes.

The open command is openning up the pickle file, you have to give its exact
location.
"""
date = '013017'
shot = 2

with open('/Users/ccartagena/Carlos/Pickle_files/mag' 
              + date + '_'+  str(shot) +'_data.pickle') as f:
    time, bdot, timeb, b, bmod = pickle.load(f)
    


def sine_plot2(date, shot, pos, xbAvg, ybAvg, title):
    
    # Overall Figure with two subplots
    fig = plt.figure(num = 2)
    
    # Setting the two subplots
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    
    #fig.suptitle(title)
    
    # Setting the axes
    
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(2)
        ax2.spines[axis].set_linewidth(2)
  
    ax1.axis([20*1.5,-5,-600,600])
    ax2.axis([20*1.5,-5,-600,600])
    
    ax1.minorticks_on()
    ax2.minorticks_on()
    
    for tick in ax1.xaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = False
    
    ax1.tick_params(which = 'both', width = 2)
    ax1.tick_params(which = 'major', length = 5)
    ax1.tick_params(which = 'minor', length = 3)
    ax2.tick_params(which = 'both', width = 2)
    ax2.tick_params(which = 'major', length = 5)
    ax2.tick_params(which = 'minor', length = 3)
    
    ax1.set_ylabel('B (G)', fontweight = 'bold',size = 16)
    ax2.set_ylabel('B (G)', fontweight = 'bold',size = 16)
    ax2.set_xlabel('Position (cm)', fontweight = 'bold', size = 16)
        # Indicator Vertical Lines
    ax1.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
    ax1.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
    ax1.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
    ax2.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
    ax2.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
    ax2.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)
    
    
    # Setting Figure title
    fig.text(0.2167,0.925,'Taylor state entering the SFC at 50.5${\mu}s$',size = 17,fontweight = 'bold')
    
    # Setting Figure text
    fig.text(0.725,0.49, 'End of SFC', color = 'grey',size = 16)
    fig.text(0.02,0.49, 'Beginning of SFC', color = 'grey',size = 16)
    fig.text(0.27,0.49, 'Triplet IDS/HeNe',size = 16)
    #fig.text(0.8,0.925,'50.5 ${\mu}s$',size = 16)
    ax1.text(0.015,0.875, r'(x)', transform = ax1.transAxes,size = 16)
    ax2.text(0.015,0.875, r'(y)', transform = ax2.transAxes,size = 16)

    # Plotting the data
    ax1.plot(pos[::-1], xbAvg[::-1], 'ro', color = 'firebrick', markersize = 10, linestyle = 'dotted',
             markeredgewidth = 0.0,linewidth = 2)
    ax2.plot(pos[::-1], ybAvg[::-1], 'bo', color = 'firebrick', markersize = 10, linestyle = 'dotted',
             markeredgewidth = 0.0, linewidth = 2)
    
    # Saving the overall figure
    savefile = 'mjmag_' + date + '_' + str(shot) + '_' + title + '.png'
    fig.savefig(savefile,dpi = 600)
    plt.close(fig)
#--------------------------------------

def plot_25avg_xypos_mag(date, shot, b, timeb, istep, fstep):
    

    pos = np.arange(20)*1.5 - 2.86
        
    while(istep < fstep):
        xbAvg = xmagneticTimeAvg(b, istep, istep + 25)
        ybAvg = ymagneticTimeAvg(b, istep, istep + 25)
        title = ( str(round(timeb[istep],1)) + '-' + str(round(timeb[istep + 25],1)))
        sine_plot2(date, shot, pos, xbAvg, ybAvg, title)
        istep = istep + 25
#--------------------------


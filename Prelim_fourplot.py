e#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:39:55 2017

@author: ccartagena
"""

import pickle
import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gds


#--------------------------------------
# Averaging ten time steps from initial time step(istep) to
# final time step(fstep). x direction
#--------------------------------------
def xmagneticTimeAvg(istep, fstep):
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
def ymagneticTimeAvg(istep, fstep):
    ybAvg = np.zeros(20)
    for i in range(0,20):
        for j in range(istep,fstep):
            ybAvg[i] = ybAvg[i] + b[1,i,j]/(fstep - istep + 1)
    return ybAvg
#--------------------------------------

date = '123016'
shot = 92

with open('/Users/ccartagena/Carlos/Pickle_files/mag' 
              + date + '_'+  str(shot) +'_data.pickle') as f:
    time, bdot, timeb, b, bmod = pickle.load(f)

L = [[2100,2125], [2225,2250], [2400,2425], [2500,2525]]

title1 = str(round(timeb[2100],1)) + '-' + str(round(timeb[2125],1)) + 'us'
title2 = str(round(timeb[2225],1)) + '-' + str(round(timeb[2250],1)) + 'us'
title3 = str(round(timeb[2400],1)) + '-' + str(round(timeb[2425],1)) + 'us'
title4 = str(round(timeb[2500],1)) + '-' + str(round(timeb[2525],1)) + 'us'

xMag = []
yMag = []

for i in range(4):
    
    x = xmagneticTimeAvg(L[i][0], L[i][1])
    y = ymagneticTimeAvg(L[i][0], L[i][1])
    
    xMag.append(x)
    yMag.append(y)
    

pos = np.arange(20) * 1.5 - 2.86
#Starting point of the figure setup            
fig = plt.figure(dpi = 80, facecolor = 'w', edgecolor = 'k')

# Setting Figure title
fig.suptitle(date + 'r' + str(shot), size = 18)

# Dividing up the figure into four sections
gs1 = gds.GridSpec(2,4)
gs1.update(left = 0.05, right = 0.95, wspace = 0.04, hspace = 0.09)
"""
gs2 = gds.GridSpec(2,1)
gs2.update(left = 0.2775, right = 0.485, wspace = 0)

gs3 = gds.GridSpec(2,1)
gs3.update(left = 0.515, right = 0.7225, wspace = 0)

gs4 = gds.GridSpec(2,1)
gs4.update(left = 0.7525, right = 0.96, wspace = 0)
"""
# Setting the subplots within the sections

ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0],sharex = ax1, sharey = ax1)
ax3 = plt.subplot(gs1[0,1],sharex = ax1, sharey = ax1)
ax4 = plt.subplot(gs1[1,1],sharex = ax1, sharey = ax1)
ax5 = plt.subplot(gs1[0,2],sharex = ax1, sharey = ax1)
ax6 = plt.subplot(gs1[1,2],sharex = ax1, sharey = ax1)
ax7 = plt.subplot(gs1[0,3],sharex = ax1, sharey = ax1)
ax8 = plt.subplot(gs1[1,3],sharex = ax1, sharey = ax1)

# Setting the axes
ax1.axis([-3,20*1.5,-600,600])
"""
ax2.axis([0,20*1.5,-600,600])
ax3.axis([0,20*1.5,-600,600])
ax4.axis([0,20*1.5,-600,600])
ax5.axis([0,20*1.5,-600,600])
ax6.axis([0,20*1.5,-600,600])
ax7.axis([0,20*1.5,-600,600])
ax8.axis([0,20*1.5,-600,600])
"""
ax1.minorticks_on()
ax2.minorticks_on()
ax3.minorticks_on()
ax4.minorticks_on()
ax5.minorticks_on()
ax6.minorticks_on()
ax7.minorticks_on()
ax8.minorticks_on()

for tick in ax1.xaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False

for tick in ax3.xaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False

for tick in ax3.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False

for tick in ax4.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False

for tick in ax5.xaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False
    
for tick in ax5.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False
    
for tick in ax6.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False
    
for tick in ax7.xaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = False


ax7.yaxis.tick_right()
ax8.yaxis.tick_right()

   
make_invisible = True
if (make_invisible):
    xticks = ax2.xaxis.get_major_ticks()
    xticks[-1].label1.set_visible(False)
if (make_invisible):
    xticks = ax4.xaxis.get_major_ticks()
    xticks[-1].label1.set_visible(False)
if (make_invisible):
    xticks = ax6.xaxis.get_major_ticks()
    xticks[-1].label1.set_visible(False)

"""
if (make_invisible):
    yticks = ax1.yaxis.get_major_ticks()
    yticks[0].label1.set_visible(False)
if (make_invisible):
    yticks = ax7.yaxis.get_major_ticks()
    yticks[0].label1.set_visible(False)
"""


ax1.set_ylabel('B [G]')
ax2.set_ylabel('B [G]')
ax2.set_xlabel('Position [cm]')
ax4.set_xlabel('Position [cm]')
ax6.set_xlabel('Position [cm]')
ax7.set_ylabel('B [G]')
ax7.yaxis.set_label_position('right')
ax8.set_ylabel('B [G]')
ax8.set_xlabel('Position [cm]')
ax8.yaxis.set_label_position('right')

# Indicator Vertical Lines

ax1.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax1.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax1.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
ax2.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax2.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax2.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)

ax3.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax3.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax3.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
ax4.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax4.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax4.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)

ax5.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax5.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax5.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
ax6.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax6.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax6.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)

ax7.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax7.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax7.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)    
ax8.axvline(x = 0, linestyle = 'dotted', color = 'grey', linewidth = 2)
ax8.axvline(x = 18.89, linestyle = 'dotted', color = 'black', linewidth = 2)
ax8.axvline(x = 29.69, linestyle = 'dotted', color = 'grey', linewidth = 2)

# Setting text
fig.text(0.015,0.87, r'(x)')
fig.text(0.015,0.455, r'(y)')
fig.text(0.24,0.925, 'Beginning of FC', color = 'grey',size = 10)
fig.text(0.04,0.925, 'End of FC', color = 'grey', size = 10)
fig.text(0.15,0.925, 'Triplet IDS/HeNe', size = 10)
fig.text(0.92,0.925, 'Beginning of FC', color = 'grey',size = 10)
fig.text(0.7225,0.925, 'End of FC', color = 'grey', size = 10)
fig.text(0.83,0.925, 'Triplet IDS/HeNe', size = 10)
fig.text(0.136,0.49, title1)
fig.text(0.364,0.49, title2)
fig.text(0.59,0.49, title3)
fig.text(0.8175,0.49, title4)

#Plotting the data
ax1.plot(pos, xMag[0], 'ro', linestyle = 'dotted')
ax2.plot(pos, yMag[0], 'bo', linestyle = 'dotted')
ax3.plot(pos, xMag[1], 'ro', linestyle = 'dotted')
ax4.plot(pos, yMag[1], 'bo', linestyle = 'dotted')
ax5.plot(pos, xMag[2], 'ro', linestyle = 'dotted')
ax6.plot(pos, yMag[2], 'bo', linestyle = 'dotted')
ax7.plot(pos, xMag[3], 'ro', linestyle = 'dotted')
ax8.plot(pos, yMag[3], 'bo', linestyle = 'dotted')



plt.show()
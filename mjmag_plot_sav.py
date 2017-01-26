#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:13:40 2017
This script creates and saves all figures
@author: ccartagena
"""

import numpy as np
import matplotlib.pylab as plt
import pickle

with open('mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)

for j in range(0,20):   
    plt.figure()
    plt.title('Y Probe ' + str(j + 1))
    plt.plot(timeb,b[1,j,:])
    plt.xlabel('Time [us]')
    plt.ylabel('B [G]')
    plt.savefig('Y_Probe_' + str(j + 1))
    plt.close()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:43:57 2017
This file was created because I did not want to rerun the data reduction.
@author: ccartagena
"""

import process_mjmag_data as mj
import numpy as np
import matplotlib.pylab as plt
import pickle

#date='123016'
#shot=1

#load mj probe data [xyz,position,timestep]
#time = time index [8192]
#bdot = calibrated dB/dt data [3,25,8192]
#timeb = time index for integrated data [8191]
#b = integrated magnetic field data [3,25,8192]
#bmod = modulus of b for doublets and triplets
def mjmag_sav(date, shot):
    
    time,bdot,timeb,b,bmod,fulldata = mj.process_mjmag_data(date+str(shot))
    
    with open('/Users/ccartagena/Carlos/Pickle_files/mag' + date + '_'
            + str(shot) + '_data.pickle','w') as f:
        pickle.dump([time,bdot,timeb,b,bmod],f)


for i in range(1,101):
    
    mjmag_sav('123016',i)

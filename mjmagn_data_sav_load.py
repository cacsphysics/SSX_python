#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:59:19 2017

@author: ccartagena
"""
import process_mjmag_data as mj
import pickle
import numpy as np

#load mj probe data [xyz,position,timestep]
#time = time index [8192]
#bdot = calibrated dB/dt data [3,25,8192]
#timeb = time index for integrated data [8191]
#b = integrated magnetic field data [3,25,8192]
#bmod = modulus of b for doublets and triplets


#--------------------------------------
# The function saves the processes the data and saves 
# it as a pickle file. 
#--------------------------------------
"""
The data parameter must be a string corresponding to the month_day_year 
without any delimiters, i.e. date = 123016 - 12/30/16

The shot parameter is an integer which corresponds to the shot number.
"""
def mjmag_sav(date, shot):
    
    time,bdot,timeb,b,bmod = mj.process_mjmag_data(date+str(shot))
    
    with open('/Users/ccartagena/Carlos/Pickle_files/mag' + date + '_'
            + str(shot) + '_data.pickle','w') as f:
        pickle.dump([time,bdot,timeb,b,bmod],f)
#--------------------------------------

#--------------------------------------
# Loading the structured data
#--------------------------------------

"""
The data parameter must be a string corresponding to the month_day_year 
without any delimiters, i.e. date = 123016 - 12/30/16

The shot parameter is an integer which corresponds to the shot number.
"""

def mjmag_load(date, shot):
    
    with open('/Users/ccartagena/Carlos/Pickle_files/mag' 
              + date + '_' +  str(shot) +'_data.pickle') as f:
       time, bdot, timeb, b, bmod = pickle.load(f)
    return time, bdot, timeb, b, bmod
#--------------------------------------
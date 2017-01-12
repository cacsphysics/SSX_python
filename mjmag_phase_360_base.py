#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:28:21 2017
 Created to correct the discontinuties
@author: ccartagena
"""

# I am creating the polar vector
import numpy as np
import matplotlib.pylab as plt
import pickle


#--------------------------------------
# Loading the structured data
#--------------------------------------
with open('mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
#--------------------------------------

#--------------------------------------
# Vector indices --- Probe Number(PN)
#--------------------------------------
probe = 9
#--------------------------------------

#--------------------------------------
# Using numpy function to obtain the first probe magnetic 
# vector angle within [-180,180]
#--------------------------------------
phi = np.zeros(7391)

for i in range(0,7391):
	phi[i] = np.arctan2(b[1, probe,i],b[0, probe,i])
phi = phi*(180)/np.pi
#--------------------------------------

#--------------------------------------
# I making the range of phi [0,360] instead of [-180,180]
#--------------------------------------
for i in range(0,7391):
	if phi[i] < 0:
		phi[i] = 360 + phi[i]
	else:
		phi[i] = phi[i]		
#--------------------------------------

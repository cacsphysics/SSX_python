#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:40:00 2017
 Created to further correct the discontinuties
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
# Vector indices --- Probe Number(pn)
#--------------------------------------
pn = 8
#--------------------------------------

#--------------------------------------
# Using numpy function to obtain the first probe magnetic 
# vector angle within [-180,180]
#--------------------------------------
phi = np.zeros(7391)

for i in range(0,7391):
	phi[i] = np.arctan2(b[1, pn,i],b[0, pn,i])
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

"""
I am removing the [0,360] restriction and going to [0,720]
Currently this is specific to probe 8, the code must be 
altered to accomodate the other probes.
"""
#--------------------------------------
# Obtaining the indicies of discontinuities
# Note that the range is shorten by one. This 
# is needed because I am comparing values and
# phi[7391] does not exist
#--------------------------------------
for i in range(0,7390):
	if phi[i] - phi[i+1] > 300:
		a = i + 1
	elif phi[i] - phi[i + 1] < -300:
		b = i
#--------------------------------------

#--------------------------------------
# Distinguishing between the lower index and the upper 
# index
#--------------------------------------
if a < b:
	lower_ind = a
	upper_ind = b
elif b < a:
	lower_ind = b
	upper_ind = a
#--------------------------------------	

#--------------------------------------
# Increasing the values between the lower index and 
# upper index by 360
#--------------------------------------
for i in range(lower_ind, upper_ind + 1):
	phi[i] = phi[i] + 360
#--------------------------------------
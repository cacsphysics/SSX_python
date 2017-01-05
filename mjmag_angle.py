 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. Currently I am figuring out how I am going to 
determine the angles between two vector positions.
"""
#mjmag_angle.py

#import process_mjmag_data as mj
import numpy as np
import matplotlib.pylab as plt

#day='123016'
#shot=92

#load mj probe data [xyz,position,timestep]
#time = time index [8192]
#bdot = calibrated dB/dt data [3,25,8192]
#timeb = time index for integrated data [8191]
#b = integrated magnetic field data [3,25,8192]
#bmod = modulus of b for doublets and triplets
#time,bdot,timeb,b,bmod = mj.process_mjmag_data(day+str(shot))

#plt.figure()
#plt.plot(timeb,b[0,0,:])
#plt.xlabel('Time [us]')
#plt.ylabel('B [G]')
j = 18
k = 19
cosine = np.zeros(7391)
# Standard cos(angle) between two vectors calculation
for i in range(0,7391):
    cosine[i] = (b[0,j,i]*b[0,k,i] + b[1,j,i]*b[1,k,i])/(bmod[j,i]*bmod[k,i])

angle = (np.arccos(cosine))*180/np.pi

plt.figure()
plt.plot(timeb, angle)
plt.xlabel('Time [us]')
plt.ylabel('phi [degrees]')
#plt.ylim(-10,185)
plt.savefig('Position_'+str(j) + str(k)+'_phase_diff.pdf')
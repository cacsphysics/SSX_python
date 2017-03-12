"""
Created on Thu Jan  5 2017

I am currently still trying to determine the phase difference;
however, this script looks promising.

Future plans are to make this a function with inputs:
"*.pickle, first_probe, second_probe".

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
first_probe = 18
second_probe = 19
#--------------------------------------

#--------------------------------------
# Using numpy function to obtain the first probe magnetic 
# vector angle within [-180,180]
#--------------------------------------
phi1 = np.zeros(7391)

for i in range(0,7391):
	phi1[i] = np.arctan2(b[1,first_probe,i],b[0,first_probe,i])
phi1 = phi1*(180)/np.pi
#--------------------------------------

#--------------------------------------
# Using numpy function to obtain the second probe magnetic 
# vector angle within [-180,180]
#--------------------------------------
phi2 = np.zeros(7391)

for i in range(0,7391):
	phi2[i] = np.arctan2(b[1,second_probe,i],b[0,second_probe,i])
phi2 = phi2*(180)/np.pi
#--------------------------------------

#--------------------------------------
# Creating the phase difference array
"""
Later I will have to adjust the definition of the phase difference,
depending on the direction of the helical plasma.
"""
#--------------------------------------
phase_diff = phi1 - phi2
#--------------------------------------

#--------------------------------------
# Plotting and saving as a pdf
#--------------------------------------
plt.figure()
plt.plot(timeb, phase_diff)
plt.xlabel('Time [us]')
plt.ylabel('phi [degrees]')
#plt.ylim(-10,185)
plt.savefig('Probe_'+str(first_probe) + str(second_probe)+'_phase_diff.pdf')
#--------------------------------------
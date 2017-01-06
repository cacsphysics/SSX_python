"""
Created on Thu Jan  5 2017

Future plans are to make this a function with inputs:
"*.pickle, probe".

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
probe = 19
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
# Plotting and saving as a pdf
#--------------------------------------
plt.figure()
plt.plot(timeb, phi)
plt.xlabel('Time [us]')
plt.ylabel('phi [degrees]')
#plt.ylim(-10,185)
plt.savefig('Probe_'+str(probe) + '_phase_diff.pdf')
#--------------------------------------
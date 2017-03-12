#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:26:23 2017

@author: ccartagena
"""

import numpy as np
import matplotlib.pylab as plt

plt.figure()
plt.clf()
plt.plot(position,bAvg,'o',linestyle = 'dotted' )
#plt.plot(position,bAvg,'o')
plt.xlabel('Position [cm]')
plt.ylabel('B [G]')
c = 'Check This Out'
plt.title(c)

distance = np.zeros(1050)

for i in range(0,1050):
    distance[i] = 0.0285 * i
sine_data = 62.94 * np.sin((1.54*distance +  m.pi)) + 6.94

#plt.plot(distance, sine_data)
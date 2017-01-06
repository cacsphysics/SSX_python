#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:31:51 2017
This file was created because I did not want to rerun the data reduction.
@author: ccartagena
"""

import pickle
import numpy as np


with open('mag123016_92_data.pickle') as f:
    time,bdot,timeb,b,bmod = pickle.load(f)
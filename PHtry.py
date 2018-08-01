#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 01:41:51 2018

@author: cx513
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:42:44 2018

@author: cx513
"""

import numpy as np
import dionysus as d
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from math import log
from math import cos
from math import sin
from math import pi
import math
import random
import pandas as pd
from TimeCounter import timer

from scipy.spatial import distance

def E3view(arr,elevation=45,azimuth=30):
    #3D illustration
    fig = pyplot.figure()
    ax = Axes3D(fig)
    ax.view_init(elev=elevation, azim=azimuth)
    ax.scatter(arr[:,0],arr[:,1],arr[:,2])
    pyplot.show()
    return ax


#TO BE ADDED:
#Each point cloud as an instance of a class
#And most functions included as methods.

def PersistentDiagram(nparray,dim=1,skeletondim=2):
    stime=timer()
    DisM=distance.pdist(nparray,'euclidean')
    M=DisM.max()
    VRC=d.fill_rips(nparray,skeletondim,M)
    ph=d.homology_persistence(VRC)
    dgms=d.init_diagrams(ph,VRC)
    timer(stime)
    return dgms[dim]


def geomill(arr,dim=1,cutoff=2,elevation=45,azimuth=30):
    #E3view(arr,elevation,azimuth)
    #VR complex
    stime=timer()
    skeletondim=dim+1
    filtration = d.fill_rips(arr, skeletondim, cutoff)
    #persistent homology
    ph = d.homology_persistence(filtration)
    dgms = d.init_diagrams(ph, filtration)
    d.plot.plot_bars(dgms[dim], show = True)
    timer(stime)
    return dgms


#filt = d.fill_rips(circ, 2, 2)

#phh = d.homology_persistence(filt)

#dgms = d.init_diagrams(phh, filt)

#d.plot.plot_bars(dgms[1], show = True)
from sklearn import datasets, linear_model

class linearreg():
    def __init__(self,Xtrain,Ytrain):
        # [n_samples,n_features]
        self.regr = linear_model.LinearRegression()
        # Train the model using the training sets
        self.regr.fit(Xtrain, Ytrain)
        
    def predict(self,Xtest):
        self.y_pred = round(np.exp(self.regr.predict(Xtest)[0,0]))
        # Make predictions using the testing set
        print(self.y_pred,'s')
        print(round(self.y_pred/3600/24,1),'days')
        print(round(self.y_pred/86400/365.25,1),'years')
        return self.y_pred
        

def regression(Xtrain,Ytrain,Xtest):
    pass
    



X1t=np.array([[100,150,200,250,400]]).T
Y1t=np.array([[np.log(1.47),np.log(4.31),np.log(14),np.log(27.37),np.log(179.76)]]).T









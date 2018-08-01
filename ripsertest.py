#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:24:37 2018

@author: cx513
"""

import numpy as np
from ripser import ripser, plot_dgms
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
import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
from E3ClusterP import irohyoten
from TimeCounter import timer


def circle(k):
    coor=np.zeros([k,3])
    for i in range(k):
        coor[i,0]=cos(i/k*2*pi)*np.random.normal(1,0.05)
        coor[i,1]=sin(i/k*2*pi)*np.random.normal(1,0.05)
        coor[i,2]=np.random.normal(0,0.1)
    return coor

def sphere(k):
    coor=np.zeros([k,3])
    for i in range(k):
        phi=i/k*2*pi
        temp=np.random.normal(0,1,3)
        norm=math.sqrt(sum(temp**2))
        coor[i,]=temp/norm
    return coor

def E3view(arr,elevation=45,azimuth=30):
    #3D illustration
    fig = pyplot.figure()
    ax = Axes3D(fig)
    ax.view_init(elev=elevation, azim=azimuth)
    ax.scatter(arr[:,0],arr[:,1],arr[:,2])
    pyplot.show()
    return ax

def randompd(k):
    data = np.random.random((k,3))
    s=timer()
    diagrams = ripser(data,maxdim=1)['dgms']
    timer(s,4)

randompd(100)

sph=ripser(sphere(100),maxdim=2)
plot_dgms(sph['dgms'],show=True)



def geomill(arr,dim=1,cutoff=2,elevation=45,azimuth=30):
    #E3view(arr,elevation,azimuth)
    #VR complex
    skeletondim=dim+1
    filtration = d.fill_rips(arr, skeletondim, cutoff)
    #persistent homology
    ph = d.homology_persistence(filtration)
    dgms = d.init_diagrams(ph, filtration)
    d.plot.plot_bars(dgms[dim], show = True)
    return dgms



def plotly3d(inputdata,samplingratio=1):
    """
    plot 3d points
    """
    plottingdata=[]
    index=np.array(range(len(inputdata)))+1
    ##Create color assignment
    colorlist = sns.color_palette("hls", len(inputdata))
    colorlist=irohyoten(colorlist)
    #Start to creat stratified plotting data
    sliced=inputdata
    colorsliced=colorlist
    length=len(sliced)
    draw=random.sample(range(length),int(length*samplingratio))
    trace0= go.Scatter3d(
            x= sliced[draw,0],
            y= sliced[draw,1],
            z= sliced[draw,2],
            mode= 'markers',
            marker= dict(size= 3,
                line= dict(width=1),
                color= colorsliced[draw],
                opacity= 0.5
                ),
            #name is the same for all points in this loop
            name= 'placeholder',
            #text is an array of size sliced
            text= index[draw]
            ) # The hover text goes here... 
    plottingdata.append(trace0);
    #Configure the layout
    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
     
    fig= go.Figure(data=plottingdata, layout=layout)
    output=py.plot(fig, auto_open=False,fileopt='new')
    return output    





####Linear regression model to estimate the time required to compute
####Pan-parameter persistent homology for n points.
from sklearn import datasets, linear_model

class linearreg():
    def __init__(self,Xtrain,Ytrain):
        # [n_samples,n_features]
        self.regr = linear_model.LinearRegression()
        # Train the model using the training sets
        self.regr.fit(Xtrain, Ytrain)
        
    def predict(self,Xtest):
        self.y_pred = round(np.exp(self.regr.predict(Xtest)[0,0]),4)
        # Make predictions using the testing set
        print(self.y_pred,'s')
        print(round(self.y_pred/3600/24,1),'days')
        print(round(self.y_pred/86400/365.25,1),'years')
        return self.y_pred
        

def regression(Xtrain,Ytrain,Xtest):
    pass

X1t=np.array([[100,200,300,400,500,600,800,1000]]).T

Y1t=np.array([[np.log(0.0062),np.log(0.0242),\
               np.log(0.0541),np.log(0.1101),\
               np.log(0.1643),np.log(0.2508),\
               np.log(0.5365),np.log(1.01)]]).T
    
plt.scatter(X1t,Y1t)






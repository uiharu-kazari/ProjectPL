ra#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:45:18 2018

@author: cx513
"""

import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')
import plotly.plotly as py
import plotly.graph_objs as go
import warnings
import random
import numpy as np
from E3ClusterP import irohyoten


def plotly3dDrawOutlier(inputdata,clusterer,percen,samplingratio=1):
    """
    plot 3d with cluster
    """
    labels=clusterer.labels_
    labelset=set(labels)
    plottingdata=[]
    index=np.array(range(len(inputdata)))+1
    ##Create color assignment
    color_palette=[sns.color_palette("hls", 8)[0]]
    #data with label -1 will be assigned
    #color (0.5,0.5,0.5), which corresponds to grey
    threshold=np.percentile(clusterer.outlier_scores_,percen)
    colorlist = [color_palette[0] if ol >= threshold
                  else (0.9, 0.9, 0.9)
                  for ol in clusterer.outlier_scores_]
    colorlist=irohyoten(colorlist)
    #print(colorlist)
    #Start to creat stratified plotting data
    for i in labelset:
        sliced=inputdata[labels==i]
        length=len(sliced)
        colorsliced=colorlist[labels==i]
        indexsliced=index[labels==i]
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
                name= 'cluster'+str(i),
                #text is an array of size sliced
                text= index[labels==i][draw]
                ) # The hover text goes here... 
        plottingdata.append(trace0);
    #Configure the layout
    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
     
    fig= go.Figure(data=plottingdata, layout=layout)
    output=py.plot(fig, auto_open=False)
    return output    

#random.sample(range(10),4)
#DN1=tSNE(X1_normalized[:2000],False,n_components=3)
#DN1=tSNE(X1_normalized[random.sample(range(100000),4000)],False,n_components=3)
"""
    layout
    
    layout= go.Layout(
            title= 'Clusters',
            hovermode= 'closest',
            xaxis= dict(
                    title= 'x',
                    ticklen= 5,
                    zeroline= True,
                    gridwidth= 2,
            ),
            yaxis=dict(
                    title= 'y',
                    ticklen= 5,
                    zeroline= True,
                    gridwidth= 2,
            ),
            zaxis=dict(
                    title= 'z',
                    ticklen= 5,
                    zeroline= True,
                    gridwidth= 2,
            ),
            showlegend= False
            )  
"""

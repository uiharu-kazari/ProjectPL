#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:11:23 2018

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

#class DimensionIncompatibleWarning(UserWarning):
#    pass

class DimensionError(Exception):
    pass

def NarrtoStr(array):
        return str(round(array[0]))+\
                ','+str(round(array[1]))+\
                ','+str(round(array[2]))


def irohyoten(ColorList):
    npa=np.array(ColorList)
    npa=npa*255
    result=[]
    for i in range(len(npa)):
#        print(npa[i])
        temp='rgb('+NarrtoStr(npa[i])+')'
        result.append(temp)
    return np.array(result)


def plotly3dDrawCl(inputdata,clusterer,samplingratio=1,extlabels=False,extNames=False,Title=False):
    """
    plot 3d with cluster
    externallabels shall be a numpy array
    """
    if type(extlabels)!=bool:
        labels=extlabels
    else:
        labels=clusterer.labels_
    labelset=set(labels)
    plottingdata=[]
    index=np.array(range(len(inputdata)))+1
    ##Create color assignment
    color_palette=sns.color_palette('Paired', len(labelset))
    #data with label -1 will be assigned
    #color (0.5,0.5,0.5), which corresponds to grey 
    if type(extlabels)!=bool:
        cluster_colors = [color_palette[x-1] for x in labels]
        colorlist=irohyoten(cluster_colors)
    else:
        cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in labels]
        cluster_member_colors = [sns.desaturate(x, p) for x, p in
                         zip(cluster_colors, clusterer.probabilities_)]
        colorlist=irohyoten(cluster_member_colors)
    #Change color parameters from 0~1 to 0~255
    if type(extNames)==bool:
        plotname=['cluster'+str(i) for i in labelset]
    else:
        plotname=extNames
    #Start to creat stratified plotting data
    for i,j in zip(labelset,range(len(labelset))):
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
                    opacity= 0.6
                   ),
                #name is the same for all points in this loop
                name= plotname[j],
                #text is an array of size sliced
                text= index[labels==i][draw]
                ) # The hover text goes here... 
        plottingdata.append(trace0);
    #Configure the layout
#    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
    if type(Title)==bool:
        Title='Clusters'
    layout= go.Layout(
            title= Title,
            hovermode= 'closest',
            showlegend= True
            )
     
    fig= go.Figure(data=plottingdata, layout=layout)
    output=py.plot(fig, auto_open=False)
#     fileopt='extend'
    return output    

#"<b>tSNE with the bank labelling</b>"
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

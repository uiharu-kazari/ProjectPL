#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:20:11 2018

@author: cx513
"""


TPC=dfInfiniteMerge(SL,'Date')

#short=TPC[0:20]

#window=50
#t1=PointCloudGeneratorSLW(TPC,window,2)

#url1=plotlyslider(t1['Date'],S[window-1:]['Adj Close'],t1['2-norm'],\
#             name1='SP500',name2='1-norm',\
#                 TITLE='Time Series with Rangeslider')

def calcandplot(window=50,p=1,dim=1):
    """
    User function for finally plotting the result
    window specifies the window size
    p specifies the norm used
    and dim specifies the dimension of persistent homology
    group to be calculated
    """
    pc=PointCloudGeneratorSLW(TPC,window,p,dim)
    nametag=str(p)+'-norm'
    url=plotlyslider(pc['Date'],S[window-1:]['Adj Close'],pc[nametag],\
             name1='SP500',name2=nametag)
    return url
    
    
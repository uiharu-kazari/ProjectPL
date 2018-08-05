#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:51:08 2018

@author: cx513
"""
"""
プロジェクトパーシステントランドスケープ
This project aims at reproduce results shown in paper:
Topological data analysis of financial time series: Landscapes of crashes.
"""
"""
Steps:
    1.Get Data (Done)
    2.Programming
    3.Test
    4.Get more data not in the paper

Coding Steps:
    Raw Data->Point Cloud(log return)->Persistent Diagrams
    ->Persistence Landscapes->L^p norms
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#dionysus is no longer used in this project
#import dionysus as d
import warnings
from termcolor import colored
from functools import reduce
import time
import os
from scipy.spatial import distance


###Preprocessing Procedures
###Preprocessing Procedures
###Preprocessing Procedures


def DateAdjC(array):
    """
    Select out date and adjusted closing prices
    Designed for data from yahoo! finance
    """
    return array[['Date','Adj Close']]

#Calculate log values
#Specially designed
def logValue(df,N,name=1):
    #input is a pandas frame
    array=df.copy()
    array[array.columns[N]]=np.log(array[array.columns[N]].values)
    #Reset column names:
    original_name=array.columns[N]
    if name==1:
        name=original_name
    array=array.rename(index=str, columns={original_name:name})
    #return value is a pandas frame
    return array


def dualmap(func_iter,value):
    """
    Apply multiple functions to one value, in list form.
    """
    return [func(value) for func in func_iter]








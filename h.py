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
import dionysus as d
from termcolor import colored
from functools import reduce


###Preprocessing Procedures
###Preprocessing Procedures
###Preprocessing Procedures

#Read in csv file

D=pd.read_csv('DJIA.csv')
N=pd.read_csv('NASDAQ.csv')
R=pd.read_csv('RU2K.csv')
S=pd.read_csv('SP500.csv')

#Stock indicies list
SL=[D,N,R,S]


def DateAdjC(array):
    """
    Select out date and adjusted closing prices
    """
    return array[['Date','Adj Close']]

SL=list(map(DateAdjC,SL))

SL[0].columns=['Date','DJIA']
SL[1].columns=['Date','NASDAQ']
SL[2].columns=['Date','RU2K']
SL[3].columns=['Date','SP500']

#See if in adjusted close prices NaN exists.

if True in set(list(map(lambda x: x.isna().values.any(),SL))):
    print(colored("Warning! NaN in input number",'blue'))


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

#natural log of closing prices
SL=list(map(lambda x:logValue(x,1,1),SL))
#This is the end of input and preprocessing data phase






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


def DateCp(array):
    """
    Select out date and adjusted closing prices
    """
    return array[['Date','Adj Close']]

for i in range(4):
    SL[i]=DateCp(SL[i])

#

#t.loc[t['Adj Close'].values>25500]
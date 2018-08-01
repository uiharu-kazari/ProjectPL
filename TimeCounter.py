#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:14:34 2018

@author: cx513
"""

import time

def timer(start=0,precision=2):
    if start==0:
        return time.time()
    else:
        end=time.time()
    diff=end-start
    print("Time elapsed: "+str(round(diff,precision))+"s.")
    
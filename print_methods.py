#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:07:06 2018

@author: cx513
"""

import time
import random
import os

def streamingprint(prompt,interval,newline=True):
    for i in range(len(prompt)):
        print(prompt[i],end="",flush=True)
        time.sleep(interval)
    if newline==True:
        print()
    

def processing(elapsed):
    print(os.linesep)
    print("完成中",end="",flush=True)
    for i in range(3):
        time.sleep(random.uniform(0.1,0.7))
        print('.',end="")
    print()
    time.sleep(0.6)
    timer(elapsed)
    streamingprint("お待たせしました〜無事に完了です",0.055)
    time.sleep(0.8)
    streamingprint("今回のご利用を楽しみにしております",0.09,newline=False)
    time.sleep(0.7)
    streamingprint("〜にこっ",0.5)
    
def dottedAnimation(func):
    def wrapper(*args,**kwargs):
        output=func(args[0])
        l=len(output)
        if l>10:
            interval=0.5/l
            dots=7
        else:
            interval=0.05
            dots=3
        streamingprint(output,interval,newline=False)
        for i in range(dots):
            time.sleep(random.uniform(0.2,0.25))
            print('.',end="")
    return wrapper

@dottedAnimation
def dottedprint(str):
    return str

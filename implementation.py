#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:20:11 2018

@author: cx513
"""

##
#Implementation Phase
##

#Read in csv file

D=pd.read_csv('DJIA.csv')
N=pd.read_csv('NASDAQ.csv')
R=pd.read_csv('RU2K.csv')
S=pd.read_csv('SP500.csv')

#Stock indicies list
SL=[D,N,R,S]

SL=list(map(DateAdjC,SL))


SL[0].columns=['Date','DJIA']
SL[1].columns=['Date','NASDAQ']
SL[2].columns=['Date','RU2K']
SL[3].columns=['Date','SP500']

#See if in adjusted close prices NaN exists.

if True in set(list(map(lambda x: x.isna().values.any(),SL))):
    warnings.warn(colored("Warning! NaN in input number",'blue'),SyntaxWarning)

#natural log of closing prices
SL=list(map(lambda x:logValue(x,1,1),SL))
#SL is a list
#This is the end of input and preprocessing data phase


TPC=dfInfiniteMerge(SL,'Date')


plotly.tools.get_credentials_file()

#short=TPC[0:20]

#window=50
#t1=PointCloudGeneratorSLW(TPC,window,2)

#url1=plotlyslider(t1['Date'],S[window-1:]['Adj Close'],t1['2-norm'],\
#             name1='SP500',name2='1-norm',\
#                 TITLE='Time Series with Rangeslider')

def calcandplot(WindowSize=50,p=1,dim=1,TITLE='Time Series with Rangeslider'):
    """
    User function for finally plotting the result
    p specifies the norm used
    and dim specifies the dimension of persistent homology
    group to be calculated
    """
    prompt1="Plotly account currently in use:"
    print(prompt1+' '+plotly.tools.get_credentials_file()['username']+'.')
    time.sleep(0.5)
    prompt2="Please refer to the readme file if you want to customize the account in use."
    streamingprint(prompt2,0.02)
    dottedprint('Computation in progress')
    st=timer()
    pc=PointCloudGeneratorSLW(TPC,WindowSize,p,dim)
    nametag=str(p)+'-norm'
    url=plotlyslider(pc['Date'],S[WindowSize-1:]['Adj Close'],pc[nametag],\
             name1='SP500',name2=nametag,TITLE=TITLE)
    processing(st)
    return url
    
    
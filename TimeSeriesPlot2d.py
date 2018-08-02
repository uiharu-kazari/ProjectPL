#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:44:49 2018

@author: cx513
"""


import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import pandas_datareader.data as web
#import quandl
#quandl.ApiConfig.api_key = "bi9w2Bj4FGiMCpUGA153"
#quandl.ApiConfig.api_version = '2015-04-09'





def plotlyslider(date,Y1,Y2,name1='1',name2='2',\
                 TITLE='Time Series with Rangeslider'):

    trace_1 = go.Scatter(
            x=date,
            y=Y1,
            name = name1,
            yaxis='y',
            line = dict(color = '#17BECF',width=3),
            opacity = 0.8)

    trace_2 = go.Scatter(
            x=date,
            y=Y2,
            name = name2,
            yaxis='y2',
            line = dict(color = '#7F7F7F'),
            opacity = 0.8)

    data = [trace_1,trace_2]

    layout = dict(
            title=TITLE,
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1m',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6m',
                             step='month',
                             stepmode='backward'),
                        dict(count=1,
                             label='YTD',
                             step='year',
                             stepmode='todate'),
                        dict(count=1,
                             label='1y',
                             step='year',
                             stepmode='backward'),
                        dict(count=3,
                             label='3y',
                             step='year',
                             stepmode='backward'),
                        dict(count=5,
                             label='5y',
                             step='year',
                             stepmode='backward'),
                        dict(count=10,
                             label='10y',
                             step='year',
                             stepmode='backward'),
                        dict(step='all')
                        ])
                ),
            rangeslider=dict(
                visible = True
            ),
                type='date'
            ),
        yaxis=dict(
            title=name1,
            titlefont=dict(
                    color= '#17BECF'
            ),
            tickfont=dict(
                    color='#17BECF'
        )
        ),
        yaxis2=dict(
            title=name2,
            titlefont=dict(
                color= '#7F7F7F'
            ),
            tickfont=dict(
                color='#7F7F7F'
            ),
            overlaying='y',
            side='right'
            )   
    )

    fig = dict(data=data, layout=layout)
    #fileopt='overwrite'
    url=py.plot(fig,auto_open=False,filename='new',fileopt='new')
    return url



#demo
#df = web.DataReader('AAPL', 'iex',datetime(2014, 10, 1),datetime(2018, 4, 1))

#plotlyslider(df.index,df['close'],df['volume'])

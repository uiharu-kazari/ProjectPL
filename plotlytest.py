#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:59:38 2018

@author: cx513
"""

import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

N = 500
x = np.linspace(0, 1, N)
y = np.random.randn(N)
df = pd.DataFrame({'x': x, 'y': y})
df.head()

data = [
    go.Scatter(
        x=df['x'], # assign x as the dataframe column 'x'
        y=df['y']
    )
]
# IPython notebook
# py.iplot(data, filename='pandas/basic-line-plot')

#url = py.plot(data, filename='basic-line-plot')

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

#Only use .iplot when using juypter
a=py.plot(data, filename = 'basic-line', auto_open=False)

#py.plot(data, filename = 'basic-line', auto_open=True)


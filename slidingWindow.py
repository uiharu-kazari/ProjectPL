#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:09:52 2018

@author: cx513
"""

#Phase Three


#Merge the four dataframes into one dataframe
#Normalize the data? Or use the log return?


def dfInfiniteMerge(dflist,colname):
    """
    Merge dataframes in dflist, according to a common column name.
    """
    return reduce(lambda left,right:pd.merge(left,right,on=colname),dflist)

TPC=dfInfiniteMerge(SL,'Date')

short=TPC[0:20]

pctest=pd.DataFrame({'Date':short['Date']})
pctest['v1']=(np.random.random(20)*100).round()
pctest['v2']=(np.random.random(20)*100).round()
pctest['v3']=(np.random.random(20)*100).round()

#define a class whose main member is a point cloud,
#and methods include computing its persistent diagram,
#output the coordinates,
#and computing the pd p-norm

def SelectedValues(df,row1,row2,col_s=1):
    """
    From row1 to row2, row2 is INCLUDED!!!
    """
    return df[df.columns[col_s:]][row1:row2+1].values

def PointCloudGeneratorSLW(dataf,window=10):
    pcloud=pd.DataFrame({'Date':dataf['Date'][window-1:]})
    l=len(pcloud)
    pcs=[SelectedValues(dataf,i,i+window-1) for i in range(l)]
    pcloud['PointCloud']=pcs
    return pcloud
    
#Integrate the following function into a class inherit 
def pdtopnorm(dgmD,p):
    bdpairs=np.array([[pt.birth,pt.death] for pt in dgmD])
    if len(bdpairs)==0:
        return 0
    return pNormBarCode(p,bdpairs)



import time

def tempPCGSLWtopNorm(PCS,p):
    pnS=pd.DataFrame({'Date':PCS['Date']})
    pnvalue=[]
    start=time.time()
    l=len(PCS)
    for i in range(l):
        pc=PCS['PointCloud'].values[i]
        pnorm=pdtopnorm(PersistentDiagram(pc),p)
        pnvalue.append(pnorm)
        marker=time.time()
        diff=round(marker-start)
        rtime=round((l-i-1)*diff/(i+1))
        print('Processing... ', diff, 's passed, ', rtime,'s left.')
#    pnvalue=[pdtopnorm()\
#             for i in range(len(PCS))]
    name=str(p)+'-'+'norm'
    pnS[name]=pnvalue
    return pnS
    
class PointCloudSeries:
    pass



#Slicing the point cloud, and calculate its persistent diagram
#Further organize the data and compute its persistence landscape

#The following code gives a toy instance for manipulating pds.
if 'pcs' in vars():
    pass
else:
    print('new')
    pcs=PointCloudGeneratorSLW(TPC,90)
test=TPC[TPC.columns[1:]][:90].values
pdia=PersistentDiagram(test)
#We will use pd[1], which gives the persistent diagram in H_1



#d.plot.plot_diagram(dgms[1], show = True)

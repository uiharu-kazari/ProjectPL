#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:09:52 2018

@author: cx513
"""

#Phase Three


#Merge the four dataframes into one dataframe
#Normalize the data? Or use the log return?

from TimeCounter import timer


def dfInfiniteMerge(dflist,colname):
    """
    Merge dataframes in dflist, according to a common column name.
    """
    return reduce(lambda left,right:pd.merge(left,right,on=colname),dflist)

TPC=dfInfiniteMerge(SL,'Date')

short=TPC[0:20]

#point cloud test
pctest=pd.DataFrame({'Date':short['Date']})
pctest['v1']=(np.random.random(20)*100).round()
pctest['v2']=(np.random.random(20)*100).round()
pctest['v3']=(np.random.random(20)*100).round()

#define a class whose main member is a point cloud,
#and methods include computing its persistent diagram,
#output the coordinates,
#and computing the pd p-norm


#Obsolete function when using dionysus package
def PersistentDiagram(nparray,dim=1,skeletondim=2):
    DisM=distance.pdist(nparray,'euclidean')
    M=DisM.max()
    VRC=d.fill_rips(nparray,skeletondim,M)
    ph=d.homology_persistence(VRC)
    dgms=d.init_diagrams(ph,VRC)
    return dgms[dim]


def PDRipser(data,dim=1):
    if dim==0:
        warnings.warn(colored("Warning! PL not defined in dim 0",'magenta'),FutureWarning)
    diagram = ripser(data,maxdim=dim)['dgms'][dim]
    return PersistenceLandscape(diagram)
    
    

def SelectedValues(df,row1,row2,col_s=1):
    """
    From row1 to row2, row2 is INCLUDED!!!
    """
    return df[df.columns[col_s:]][row1:row2+1].values

def PointCloudGeneratorSLW(dataf,window=10,p=1):
#    pcloud=pd.DataFrame({'Date':dataf['Date'][window-1:]})    
    pcloud=dataf.copy()[window-1:]
    l=len(pcloud)
    pcs=[SelectedValues(dataf,i,i+window-1) for i in range(l)]
#    pcloud['PointCloud']=pcs
    PLandscapes=map(PDRipser,pcs)
#    pcloud['PersistenceLandscape']=PLandscapes
    pnormlist=list(map(lambda ins:ins.norm(p),PLandscapes))
    newcolname=str(p)+'-norm'
    pcloud[newcolname]=pnormlist
    return pcloud

#The following code gives a toy instance for manipulating pds.
test=PointCloudGeneratorSLW(TPC[:90],10)

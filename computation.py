#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 18:33:27 2018

@author: cx513
"""


#Phase Two

#Merge the four dataframes into one dataframe
#Normalize the data? Or use the log return?

def dfInfiniteMerge(dflist,colname):
    """
    Merge dataframes in dflist, according to a common column name.
    """
    return reduce(lambda left,right:pd.merge(left,right,on=colname),dflist)

TPC=dfInfiniteMerge(SL,'Date')




#Slicing the point cloud, and calculate its persistent diagram


from scipy.spatial import distance

#TO BE ADDED:
#Each point cloud as an instance of a class
#And most functions included as methods.

def PersistentDiagram(nparray,skeletondim=2):
    DisM=distance.pdist(nparray,'euclidean')
    M=DisM.max()
    VRC=d.fill_rips(nparray,skeletondim,M)
    ph=d.homology_persistence(VRC)
    dgms=d.init_diagrams(ph,VRC)
    return dgms



#For each persistent diagram, we want to associate it with a persistence 
#landscape

def PersistentLandscape(diagram):
    pass

#If a function is defined without using numpy, it is necessary to make it
#listable via wrapper and decorators, for example.
    
def plf(bdpair):
    """
    For each point in the persistent diagram, we associate it with a 
    piecewise linear function
    bdpair is a numpy.ndarray object
    """
    b=bdpair[0]
    d=bdpair[1]
    return lambda x:np.maximum(0,np.minimum(x-b,d-x))

def dualmap(func_iter,value):
    """
    Apply multiple functions to one value, in list form.
    """
    return [func(value) for func in func_iter]

#Test this function with the diagram in 77/86
    
#Auxilary function used for adding listable attributes

#Persistence landscape function with all the k-th,
#Might be useful in calculating norms.
def muAll(bdpairs):
    """
    Return ALL plf fucntions based on a given birth-death pair
    """
    l=len(bdpairs)
    f=lambda i:plf(bdpairs[i])
    return lambda x:dualmap(list(map(f,range(l))),x)

        
def muk(k,bdpairs):
    """
    Return the k-th maximum, vector supported.
    """
    l=len(bdpairs)
    f=lambda i:plf(bdpairs[i])
    def veczeros(x):
        if isinstance(x,int) or isinstance(x,float):
            return 0
        else:
            return np.array([0]*len(x))
    if k > l:
        return lambda x:veczeros(x)
    def EvaluateAtOnePoint(x):
        values=dualmap(list(map(f,range(l))),x)
        return sorted(values,reverse=True)[k-1]
    def EvaluateAtPoints(array):
        return np.array(list(map(EvaluateAtOnePoint,array)))
    def kthM(x):
        if isinstance(x,int) or isinstance(x,float):
            return EvaluateAtOnePoint(x)
        elif isinstance(x,list) or isinstance(x,np.ndarray):
            return EvaluateAtPoints(x)
    return lambda x:kthM(x)

#Plot the landscape function
fig,ax=plt.subplots(figsize=[15,7])
x=np.linspace(0,8,800);
ax.plot(x,muk(1,bdp)(x),lw=4,color='blue',ls='--',alpha=0.5,label=r'k=1')
ax.plot(x,muk(2,bdp)(x),lw=4,color='cyan',ls='--',alpha=0.5,label=r'k=2')
ax.plot(x,muk(3,bdp)(x),lw=4,color='purple',ls='--',alpha=0.5,label=r'k=3')
ax.legend()
plt.show()


#Now we compute the norm.
import scipy.integrate as integrate
result = integrate.quad(lambda x: x, 0, 4.5)

def pNormBarCode(bdpairs):
    pass


#The following code gives a toy instance for manipulating pds.

test=TPC[TPC.columns[1:]][:90].values
pdia=PersistentDiagram(test)
#We will use pd[1], which gives the persistent diagram in H_1

bdp=np.array([(1,5),(2,7),(3,6)])
#    return lambda x:[f[i](x) for i in range(l)]
#.sort[-k]
    

#There exists analytic formulas to calculate the p-norm of a persistence
#diagram
        



#d.plot.plot_diagram(dgms[1], show = True)




#TPC[TPC.columns[1:]][:90]





#d.plot.plot_diagram(dgms[1], show = True)







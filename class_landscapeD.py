#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 23:15:48 2018

@author: cx513
"""

#Integrate the following function into a class inherit 
#Decorate a class?

class DiagramEnriched(d._dionysus.Diagram):
#    def __init__(self,pdiagram):
#        if not isinstance(pdiagram,d_dionnysus.Diagram):
#            raise Exception(TypeError)
#        self.Diagram=pdiagram
    #We use the initiator from d._dionysus.Diagram
    #empty bracket() or (2-dim array)
        
    def norm(self,p):
        bdpairs=np.array([[pt.birth,pt.death] for pt in self])
        return pNormBarCode(p,bdpairs)


        
def pdtopnorm(dgmD,p):
    bdpairs=np.array([[pt.birth,pt.death] for pt in dgmD])
    if len(bdpairs==0):
        return 0
    return pNormBarCode(p,bdpairs)
    

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

        
###
#Can use enumerate to simplify the codes in the function below
###
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
    
bdp=np.array([(1,5),(2,7),(3,6)])
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

def mukInt(p,k,bdpairs):
    """
    Calculate the integration over the nonzero zone of 
    muk to the p-th power
    """
    birth=sorted(bdpairs[:,0])
    death=sorted(bdpairs[:,1],reverse=True)
    #Notice that muk is positive semidefinite
    result=integrate.quad(lambda x:muk(k,bdpairs)(x)**p,birth[k-1],death[k-1])
    return np.array(result)
    
import const


def OneNormBarCode(bdpairs):
    """
    Direclty calculate the 1-norm of a persistent diagram
    based on analytic formulas.
    """
    return np.square(bdpairs[:,1]-bdpairs[:,0]).sum()/4

def infNormBarCode(bdpairs):
    """
    Direclty calculate the infinite norm of a persistent diagram
    based on analytic formulas.
    """
    return (bdpairs[:,1]-bdpairs[:,0]).max()

def pNormBarCode(p,bdpairs):
    """
    Compute the p-norm of a persistent diagram.
    """
    if p==1:
        return OneNormBarCode(bdpairs)
    elif p=='inf':
        return infNormBarCode(bdpairs)
    else:        
        l=len(bdpairs)
        IntRes=np.array([mukInt(p,k,bdpairs) for k in range(1,l+1)])
        Values=IntRes[:,0]
        Errors=IntRes[:,1]
        if (Errors>const.IntEpsilon).any():
            print(colored("Warning! Integration Error Too Large!!",'red'))
        return np.power(Values.sum(),1/p)

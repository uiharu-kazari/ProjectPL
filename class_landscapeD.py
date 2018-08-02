#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 23:15:48 2018

@author: cx513
"""

import dionysus as d
from ripser import ripser, plot_dgms
import const
import scipy.integrate as integrate


class PrecisionWarning(Warning):
    pass


#testPD=d._dionysus.Diagram([(1,2),(3,4)])

#Initializer for the class when using dionysus package
'''
class DiagramEnriched(d._dionysus.Diagram):
    
    def __init__(self,pdiagram):
        """
        initializer for enriched diagram
        Have to be from a dionysus diagram
        """
        points=[(pt.birth,pt.death) for pt in pdiagram]
        d._dionysus.Diagram.__init__(self,points)
        self.bdpairs=np.array(points)
        #We use the initiator from d._dionysus.Diagram
        #empty bracket() or (2-dim array)
        #Example:d._dionysus.Diagram([(1,2),(3,4)])
'''
        
        
class PersistenceLandscape():
    """
    Use ripser for this class. No need to inherit other classes
    Persistence Landscapes are not defined for dim=0
    """
    def __init__(self,nparray):
        self.bdpairs=nparray
    #If a function is defined without using numpy, it is necessary to make it
    #listable via wrapper and decorators, for example.
    
    ###
    ##Functions in persistent landscape
    ###
    def plf(self,onebdp):
        """
        For each point in the persistent diagram, we associate it with a 
        piecewise linear function
        bdpair is a numpy.ndarray object
        """
        birth=onebdp[0]
        death=onebdp[1]
        return lambda x:np.maximum(0,np.minimum(x-birth,death-x))

    #Persistence landscape function with all the k-th,
    #Might be useful in calculating norms.
    def muAll(self):
        """
        Return ALL plf fucntions of this instance
        """
        l=len(self.bdpairs)
        f=lambda i:self.plf(self.bdpairs[i])
        #dualmap is defined in h.py
        return lambda x:dualmap(list(map(f,range(l))),x)

    ###
    #Can use enumerate to simplify the codes in the function below
    ###
    def muk(self,k):
        """
        Return the k-th maximum, vector supported.
        """
        l=len(self.bdpairs)
        f=lambda i:self.plf(self.bdpairs[i])
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

    def mukInt(self,p,k):
        """
        Calculate the integration over the nonzero zone of 
        muk to the p-th power
        """
        if len(self.bdpairs)==0:
            result=0
        else:
            birth=sorted(self.bdpairs[:,0])
            death=sorted(self.bdpairs[:,1],reverse=True)
            #Notice that muk is positive semidefinite
            result=integrate.quad(lambda x:self.muk(k)(x)**p,birth[k-1],death[k-1])
        return result
    
        
    def __OneNormBarCode__(self):
        """
        Direclty calculate the 1-norm of a persistent diagram
        based on analytic formulas.
        """
        return np.square(self.bdpairs[:,1]-self.bdpairs[:,0]).sum()/4

    def __infNormBarCode__(self):
        """
        Direclty calculate the infinite norm of a persistent diagram
        based on analytic formulas.
        """
        return (self.bdpairs[:,1]-self.bdpairs[:,0]).max()

    def norm(self,p):
        """
        Compute the p-norm of a persistent diagram.
        """
        if p==1:
            return self.__OneNormBarCode__()
        elif p=='inf':
            return self.__infNormBarCode__()
        else:        
            l=len(self.bdpairs)
            if l==0:
                return 0
            IntRes=np.array([self.mukInt(p,k) for k in range(1,l+1)])
            Values=IntRes[:,0]
            Errors=IntRes[:,1]
            if (Errors>const.IntEpsilon).any():
                warnings.warn(colored("Warning!\
Integration Error Too Large!!",'magenta'),PrecisionWarning)
            return np.power(Values.sum(),1/p)

    

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 12:03:02 2022

@author: leona
"""

import numpy as np
from autograd import grad
from problems import dim
from problems import vinD
from problems import vinU
from problems import Lagr
from problems import nablaLagr

from constants import *

n = DIM

def isKKT(x, la, mu, m, p) :
    #print("Il punto x", x, "è forse KKT")
    trhd1 = 10**(-4)
    trhd2 = 10**(-5)
    
    #CONTROLLO MOLTIPLICATORE LAMBDA
    nonNegLa = True
    # if m != 0 :
    #     if (la == 0).all() :
    #         return False
        
    if m != 0 :
        if (la < 0).any() :
            return False
        
    # if m != 0 :
    #     for i in range(la.shape[0]):
    #         if la[i] < 0:
    #             return False
            
    
    #CONTROLLO COMPLEMENTARIETà#
    isComp = True
    nonCompIndex = 0
    for i in range(m):
        if np.linalg.norm(vinD(x)[i] * la[i]) > 10**(-5): 
            # se almeno un lambda_i*g_i > 0 allora non complementare
            nonCompIndex = i
            isComp = False
    
    #CONTROLLO LAGRANGIANA#
    nullGradLagr = False
    if np.linalg.norm(nablaLagr(Lagr, x, la, mu, n)) <= trhd1 :
        nullGradLagr = True
    # print("norma gradiente lagrangiana", np.linalg.norm(nablaLagr(Lagr, x, la, mu, n)))
    # print("nullGradLagr", nullGradLagr)
    
    #CONTROLLO AMMISSIBILITà#
    ammD = True
    ammU = True

    if np.any(vinD(x) > trhd2):
        ammD = False

    for j in range(p):
        if np.linalg.norm(vinU(x)[j]) >= trhd2 :
            ammU = False
            
    print("vinD ", vinD(x))
    print("ammD", ammD)
    print("ammU", ammU)
    print("isComp", isComp, "norm", np.linalg.norm(vinD(x)[nonCompIndex] * la[nonCompIndex]))
    print("nullGradLagr", nullGradLagr)
    
    if ammD and ammU and isComp and nullGradLagr : 
        return True
    else : 
        return (False, nonNegLa, ammD, ammU, isComp, nullGradLagr)
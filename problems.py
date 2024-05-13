import numpy as np
from autograd import grad

from constants import *

'''
m = 2
p = 2

def starting_point(n) :
    return np.array([10., 10., 10., 10.])

def dim() :
    return 4

def functionP(x, n): 
    return -x[0]

def vincoliP(x): #funzione di penalità
    return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

def P(x, eps, n): #funzione di penalità
    return functionP(x, n) + (1 / eps) * vincoliP(x)
    
def vinD(x) :
    g1 = x[0]**3 - x[1]
    g2 = x[1] - x[0]**2
    return np.array([g1, g2])

def vinU(x) :
    h1 = x[1] - x[0]**3 - x[2]**2
    h2 = x[0]**2 - x[2] - x[3]**2
    return np.array([h1, h2])

def Lagr(x, la, mu, n) :
    L = functionP(x, n)
    constraintsD = vinD(x)
    constraintsU = vinU(x)
    for i in range(m) :
        L += constraintsD[i] * la[i]
        
    for j in range(p) :
        L += constraintsU[j] * mu[j]
    return L

def nablaLagr(Lagr, x, la, mu, n) :
    return grad(Lagr)(x, la, mu, n)
'''

"""
### FILE4 - 2 ###

m = 0
p = 2

def dim() :
    return 3

def starting_point(n) :
    return np.array([0., 0., 0.])

def functionP(x, n):
    return 4*x[0]**2 + 2*x[1]**2 + 2*x[2]**2 - 33*x[0] + 16*x[1] - 24*x[2]

def vinD(x) :
    #g1
    #gm
    return np.array([])

def vinU(x) :
    h1 = 3*x[0] - 2*x[1]**2 - 7
    h2 = 4*x[0] - x[2]**2 - 11
    #hp
    return np.array([h1, h2])

def vincoliP(x): #funzione di penalità
    return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

def P(x, eps, n): #funzione di penalità
    return functionP(x, n) + (1 / eps) * vincoliP(x)
    
def Lagr(x, la, mu, n) :
    L = functionP(x, n)
    for i in range(m) :
        L += vinD(x)[i] * la[i]
    #print("Lla", Lla)
    for j in range(p) :
        L += vinU(x)[j] * mu[j]
    #print("Lmu", Lmu)
    return L

def nablaLagr(Lagr, x, la, mu, n) :
    return grad(Lagr)(x, la, mu, n)
"""


### FILE5 - 2 ###

m = 9
p = 1

def dim() :
    return 4

def starting_point(n) :
    return np.array([1., 5., 5., 1.])

def functionP(x, n):
    return x[0]*x[3]*(x[0] + x[1] + x[2]) + x[2]

def vinD(x) :
    g1 = - x[0]*x[1]*x[2]*x[3] + 25
    g2 = 1 - x[0]
    g3 = x[0] - 5
    g4 = 1 - x[1]
    g5 = x[1] - 5
    g6 = 1 - x[2]
    g7 = x[2] - 5
    g8 = 1 - x[3]
    g9 = x[3] - 5
    #gm
    return np.array([g1, g2, g3, g4, g5, g6, g7, g8, g9])

def vinU(x) :
    h1 = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 - 40
    #hp
    return np.array([h1])

def vincoliP(x): #funzione di penalità
    return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

def P(x, eps, n): #funzione di penalità
    return functionP(x, n) + (1 / eps) * vincoliP(x)
    
def Lagr(x, la, mu, n) :
    L = functionP(x, n)
    for i in range(m) :
        L += vinD(x)[i] * la[i]
    #print("Lla", Lla)
    for j in range(p) :
        L += vinU(x)[j] * mu[j]
    #print("Lmu", Lmu)
    return L

def nablaLagr(Lagr, x, la, mu, n) :
    return grad(Lagr)(x, la, mu, n)
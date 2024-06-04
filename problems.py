import numpy as np
from autograd import grad

from constants import *


# m = 2
# p = 2

# def starting_point(n) :
#     return np.array([10., 10., 10., 10.])

# def dim() :
#     return 4

# def functionP(x, n): 
#     return -x[0]

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def vinD(x) :
#     g1 = x[0]**3 - x[1]
#     g2 = x[1] - x[0]**2
#     return np.array([g1, g2])

# def vinU(x) :
#     h1 = x[1] - x[0]**3 - x[2]**2
#     h2 = x[0]**2 - x[2] - x[3]**2
#     return np.array([h1, h2])

# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     constraintsD = vinD(x)
#     constraintsU = vinU(x)
#     for i in range(m) :
#         L += constraintsD[i] * la[i]
        
#     for j in range(p) :
#         L += constraintsU[j] * mu[j]
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)



### FILE4 - 2 ###

# m = 0
# p = 2

# def dim() :
#     return 3

# def starting_point(n) :
#     return np.array([0., 0., 0.])

# def functionP(x, n):
#     return 4*x[0]**2 + 2*x[1]**2 + 2*x[2]**2 - 33*x[0] + 16*x[1] - 24*x[2]

# def vinD(x) :
#     #g1
#     #gm
#     return np.array([])

# def vinU(x) :
#     h1 = 3*x[0] - 2*x[1]**2 - 7
#     h2 = 4*x[0] - x[2]**2 - 11
#     #hp
#     return np.array([h1, h2])

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     for i in range(m) :
#         L += vinD(x)[i] * la[i]
#     #print("Lla", Lla)
#     for j in range(p) :
#         L += vinU(x)[j] * mu[j]
#     #print("Lmu", Lmu)
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)



### FILE5 - 2 ###

# m = 9
# p = 1

# def dim() :
#     return 4

# def starting_point(n) :
#     return np.array([1., 5., 5., 1.])

# def functionP(x, n):
#     return x[0]*x[3]*(x[0] + x[1] + x[2]) + x[2]

# def vinD(x) :
#     g1 = - x[0]*x[1]*x[2]*x[3] + 25
#     g2 = 1 - x[0]
#     g3 = x[0] - 5
#     g4 = 1 - x[1]
#     g5 = x[1] - 5
#     g6 = 1 - x[2]
#     g7 = x[2] - 5
#     g8 = 1 - x[3]
#     g9 = x[3] - 5
#     #gm
#     return np.array([g1, g2, g3, g4, g5, g6, g7, g8, g9])

# def vinU(x) :
#     h1 = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 - 40
#     #hp
#     return np.array([h1])

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     for i in range(m) :
#         L += vinD(x)[i] * la[i]
#     #print("Lla", Lla)
#     for j in range(p) :
#         L += vinU(x)[j] * mu[j]
#     #print("Lmu", Lmu)
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)


### FILE1 - 4 ###

# m = 3
# p = 0

# def dim() :
#     return 2

# def starting_point(n) :
#     return np.array([-2., 1.])

# def functionP(x, n):
#     return 100*(x[1]- x[0]**2)**2 +(1-x[0])**2

# def vinD(x) :
#     g1 = -x[0]*x[1] + 1
#     g2 = -x[0] - x[1]**2
#     g3 = x[0] - 0.5
    
#     return np.array([g1, g2, g3])

# def vinU(x) :
#     return np.array([])

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     for i in range(m) :
#         L += vinD(x)[i] * la[i]
#     #print("Lla", Lla)
#     for j in range(p) :
#         L += vinU(x)[j] * mu[j]
#     #print("Lmu", Lmu)
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)


### FILE2 - 4 ###

# m = 6
# p = 0

# def dim() :
#     return 2

# def starting_point(n) :
#     return np.array([20.1 , 5.84])

# def functionP(x, n):
#     return (x[0]-10)**3 + (x[1]-20)**3

# def vinD(x) :
#     g1 = 100 - (x[0]-5)**2 - (x[1]-5)**2
#     g2 = (x[1]-5)**2 + (x[0]-6)**2 - 82.81
#     g3 = x[0] - 100
#     g4 = 13 - x[0]
#     g5 = x[1] - 100
#     g6 = -x[1]
#     return np.array([g1,g2,g3,g4,g5,g6])

# def vinU(x) :
#     return np.array([])

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     for i in range(m) :
#         L += vinD(x)[i] * la[i]
#     #print("Lla", Lla)
#     for j in range(p) :
#         L += vinU(x)[j] * mu[j]
#     #print("Lmu", Lmu)
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)



### FILE1 - 1 ###

# m = 1
# p = 0

# def dim() :
#     return 2

# def starting_point(n) :
#     return np.array([-4.9,1.])

# def functionP(x, n):
#     return (x[0]-5)**2 + (x[1])**2 - 25

# def vinD(x) :
#     g1 = x[0]**2 - x[1]
#     return np.array([g1])

# def vinU(x) :
#     return np.array([])

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     for i in range(m) :
#         L += vinD(x)[i] * la[i]
#     #print("Lla", Lla)
#     for j in range(p) :
#         L += vinU(x)[j] * mu[j]
#     #print("Lmu", Lmu)
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)



# ===================== PROBLEMI IMPLEMENTAZIONI ==========================



#PROBLEMA 1 


# m = 2
# p = 2

# def starting_point(n) :
#     return np.array([10.,10.,10.,10.])

# def dim() :
#     return 4

# def functionP(x, n): 
#     return -x[0]

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def vinD(x) :
#     g1 = -x[1]+x[0]**3
#     g2 = -x[0]**2-x[1]
    
#     return np.array([g1, g2])

# def vinU(x) :
#     h1=x[1]-x[0]**3-x[2]**2
#     h2=x[0]**2-x[1]-x[3]**2
#     return np.array([h1,h2])

# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     constraintsD = vinD(x)
#     constraintsU = vinU(x)
#     for i in range(m) :
#         L += constraintsD[i] * la[i]
        
#     for j in range(p) :
#         L += constraintsU[j] * mu[j]
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)



#PROBLEMA 2 

# m = 2
# p = 0

# def starting_point(n) :
#     return np.array([0.,0.])

# def dim() :
#     return 2

# def functionP(x, n): 
#     return x[0]**2+x[1]

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def vinD(x) :
#     g1 = x[0]+x[1]-1
#     g2 = (x[0]**2+x[1]**2)-9
#     return np.array([g1, g2])

# def vinU(x) :
    
#     return 0

# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     constraintsD = vinD(x)
#     constraintsU = vinU(x)
#     for i in range(m) :
#         L += constraintsD[i] * la[i]
        
#     for j in range(p) :
#         L += constraintsU[j] * mu[j]
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)

#PROBLEMA 3
# m = 5
# p = 0

# def starting_point(n) :
#     return np.array([3.,1.])

# def dim() :
#     return 2

# def functionP(x, n): 
#     return x[0]**2+x[1]**2

# def vincoliP(x): #funzione di penalità
#     return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

# def P(x, eps, n): #funzione di penalità
#     return functionP(x, n) + (1 / eps) * vincoliP(x)
    
# def vinD(x) :
#     g1 = -x[0]-x[1]+1
#     g2 = -x[0]**2-x[1]**2 +1
#     g3=-9*x[0]**2-x[1]**2 + 9
#     g4=-x[0]**2 +x[1]
#     g5= -x[1]**2 + x[0]
#     return np.array([g1, g2,g3,g4,g5])

# def vinU(x) :
    
#     return 0

# def Lagr(x, la, mu, n) :
#     L = functionP(x, n)
#     constraintsD = vinD(x)
#     constraintsU = vinU(x)
#     for i in range(m) :
#         L += constraintsD[i] * la[i]
        
#     for j in range(p) :
#         L += constraintsU[j] * mu[j]
#     return L

# def nablaLagr(Lagr, x, la, mu, n) :
#     return grad(Lagr)(x, la, mu, n)

#PROBLEMA 4

# DA MODIFICARE
m = 2
p = 0

# DA MODIFICARE
def starting_point(n) :
    return np.array([22.3,0.5,125.])

# DA MODIFICARE
def dim() :
    return 3

# DA MODIFICARE
def functionP(x, n): 
    return (float(-0.0201)*x[0]**4*x[1]*x[2]**2)*10**(-7)

def vincoliP(x): #funzione di penalità
    return (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))

def P(x, eps, n): #funzione di penalità
    return functionP(x, n) + (1 / eps) * vincoliP(x)

# DA MODIFICARE  
def vinD(x) :
    g1 = x[0]**2*x[1]-675
    g2 = 10**(-7)*x[0]**2*x[2]**2-float(0.419)
    
    return np.array([g1, g2])

# DA MODIFICARE
def vinU(x) :
    
    return 0

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


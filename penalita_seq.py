# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:05:22 2022

@author: leona
"""

import numpy as np
from autograd import grad
from kkt import isKKT
from problems import dim
from problems import starting_point
from problems import functionP
from problems import vinD
from problems import vinU
from problems import P
from problems import Lagr
from problems import nablaLagr
from problems import vincoliP
from newton_troncato import troncatoMAIN

from constants import *



n_iter = 0

n = DIM
x = starting_point(n) 
f = functionP(x, n)

nf = 1

la = np.zeros(m)
mu = np.zeros(p)

file = open(FILENAME_PROBLEM, "w")

while True :
    
    l = Lagr(x, la, mu, n)
    z = nablaLagr(Lagr, x, la, mu, n)
    t = np.linalg.norm(z)
    
    
    print(f"penalita iter: {n_iter}")

    #ARRESTO 1#
    if n_iter > max_iter_penalita :
        print("\nAlgoritmo terminato per massimo numero di iterazioni")
        file.write("\nAlgoritmo terminato per massimo numero di iterazioni")
        for i in range(0, n) :
            print("\nx(",i+1,") =",x[i], "\n")
            file.write("\nx("+str(i+1)+") = "+str(x[i])+ "\n")
        file.close()
        break

#PASSO 1# 

    for i in range(m) :
        la[i] = (2 / EPS[0]) * np.maximum(0, vinD(x)[i])
        
    for j in range(p) :
        mu[j] = (2 / EPS[0]) * vinU(x)[j]

    nf += 2

    #ARRESTO 2#
    if isKKT(x, la, mu, m, p) == True :
        print("Algortimo terminato con un punto KKT del problema.\nIl punto è\n")
        file.write("Algortimo terminato con un punto KKT del problema.\nIl punto è\n")
        for i in range(0, n) :
            print  ("\nx(",i+1,") =",x[i], "\n")
            file.write("\nx("+str(i+1)+") = "+str(x[i])+ "\n")
        print(f"f_value: {functionP(x, n)}")
        import sys
        sys.stdout.write('\a')
        sys.stdout.flush()
        file.close()
        break
    else :
        snnl = "lambda non negativi: " + str(la)
        smu = "moltiplicatori mu: " + str(mu)
        
        sd = "  ammissibilità vincoli di disuguaglianza: " + str(vinD(x))
        su = "  ammissibilità vincoli di uguaglianza: " + str(vinU(x))
        sic = "  complementarietà: " + str(la*vinD(x))
        sngl = "  gradiente lagrangiano sufficientemente piccolo: " + str(t)
        #sKKT = "il punto non è di KKT, perchè " + snnl + sd + su + sic + sngl
        print("n_iter_PEN_SEQ =",n_iter,"  nf_PEN_SEQ =",nf, "f_PEN_SEQ =",  f)
        sf = " f = " + str(f)
        snf = " nf = " + str(nf)
        svv = " violazione dei vincoli, disuguaglianza: " + str(vinD(x)) + " , uguaglianza : " + str(vinU(x))
        #sni = " n_iter = " + str(n_iter)
        #sl = " f Lagr = " + str(l)
        #snl = " f nablaLagr = " + str(z)
        #sgnl = " gradient nablalagr = " + str(t)
        sKKT = "il punto non è di KKT, perchè " + smu + snnl + sd + su + sic + sngl
        file.write(sf + "\t\t" + snf + "\t\t" + svv + "\t\t" + sKKT)
        file.write("\n\n")
    
#PASSO 2#
    checkR = teta1 * vincoliP(x)
    nf += 2

    xk = troncatoMAIN(EPS[1], delta, x)

    checkL = vincoliP(xk)
    nf += 1
    
#PASSO 3#
    if checkL > checkR:
        EPS.append(EPS[1] * teta2)
        EPS.pop(0)
        
    f = functionP(xk, n)
    x = xk
    
#PASSO 4#
    delta *= teta3
    n_iter += 1
    
    l = Lagr(x, la, mu, n)
    z = nablaLagr(Lagr, x, la, mu, n)
    t = np.linalg.norm(z)
    
    
    


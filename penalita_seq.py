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
f_stampe = open(FILENAME_STAMPE, "w")

while True :
    
    l = Lagr(x, la, mu, n)
    z = nablaLagr(Lagr, x, la, mu, n)
    t = np.linalg.norm(z)
    
    
    # print(f"penalita iter: {n_iter}")

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

        print("Algortimo terminato con un punto KKT del problema.\n")
        f_stampe.write("\n")
        f_stampe.write("Algortimo terminato con un punto KKT del problema.\n")
        # ============== Stampo il punto ottimo x* ==================
        print("Il punto ottimo x* è\n")
        f_stampe.write("Il punto ottimo x*\n")

        for i in range(0, n) :
            print(f"x({i+1}) = {x[i]}")
            f_stampe.write(f"x({i+1}) = {x[i]}\n")

        print()

        # ============== Stampo il valore della funzione obiettivo f(x*) ==================
        print(f"Il valore della funzione obiettivo in x* è: {functionP(x, n)}")
        f_stampe.write("\n")
        f_stampe.write(f"Il valore della funzione obiettivo in x*: {functionP(x, n)}")

        print()
        # ============== Stampo il valore dei vincoli in x* ==================
        print(f"Il valore dei vincoli in x* è: \n")
        f_stampe.write("\n")
        f_stampe.write(f"Il valore dei vincoli in x*: \n")

        for i in range(m) :
            print(f"Vincolo di disuguaglianza {i+1}: {vinD(x)[i]} \n")
            f_stampe.write(f"Vincolo di disuguaglianza {i+1}: {vinD(x)[i]} \n")


        for j in range(p) :
            print(f"Vincolo di uguaglianza {j+1}: {vinU(x)[j]} \n")
            f_stampe.write(f"Vincolo di uguaglianza {j+1}: {vinU(x)[j]} \n")


        # ============== Stampo il valore dei moltiplicatoru la* e mu* ==================
        print()
        print(f"Il valore dei moltiplicatori: \n")
        f_stampe.write(f"Il valore dei moltiplicatori: \n")

        for i in range(m) :
            print(f"Valore di lambda {i+1}: {la[i]} \n")
            f_stampe.write(f"Valore di lambda {i+1}: {la[i]} \n")


        for j in range(p) :
            print(f"Valore di mu {j+1}: {mu[j]} \n")
            f_stampe.write(f"Valore di mu {j+1}: {mu[j]} \n")


        # ============== Stampo il valore dei moltiplicatoru la* e mu* ==================
        print()
        print(f"Il Valore della norma del gradiente della Lagrangiana è: {np.linalg.norm(nablaLagr(Lagr, x, la, mu, n))}")
        f_stampe.write(f"Il Valore della norma del gradiente della Lagrangiana: {np.linalg.norm(nablaLagr(Lagr, x, la, mu, n))}")

        #Metti print finali
        '''
        f*
        x*
        VinD(x*)
        VinU(x*)
        la*
        mu*
        ||NablaLagr(x*)||
        '''
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
        f_stampe.write(f"n_iter_PEN_SEQ = {n_iter} nf_PEN_SEQ= {nf} f_PEN_SEQ= {f} ")
        
        kkt_constraint = (np.sum(np.maximum(0.0, vinD(x))) + np.sum(np.abs(vinU(x))))
        # kkt_constraint = (np.sum((np.maximum(0.0, vinD(x)))**2) + (np.sum(vinU(x)**2)))
        f_stampe.write(f"Il punto non soddisfa le condizioni di KKT per la seguente violazione di ammissibilita: {kkt_constraint}\n")

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
    
    
    


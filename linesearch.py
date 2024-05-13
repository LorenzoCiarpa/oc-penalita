# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:35:41 2022

@author: leona
"""

import numpy as np

def linesearch_ArmijoNonMonotona(l, f, function, x, n, gamma, alpha, direction, gradient_dir, nf, eps) :
    
    alpha = 0.5
    #print(alpha)
    y = np.zeros(n)
    y = x + alpha*direction
    #print("y", y)
    phi_alpha = function(y, n, eps)
    #print(phi_alpha, f, alpha, gamma, gradient_dir)
    nf += 1
    M = 10
    
    if len(l) < 10 :
        while phi_alpha > f + alpha*gamma*gradient_dir : 
        
            alpha = alpha * (0.5)
            print(alpha)
            y = x + alpha*direction
            #print("y", y)
            phi_alpha = function(y, n, eps)
            #print("phi_alpha", phi_alpha)
            nf += 1
            #print("loop")
            print("scarto", phi_alpha - f - alpha*gamma*gradient_dir)

    else :
        
        while phi_alpha > max(l[-M:]) + alpha*gamma*gradient_dir : 
    
            alpha = alpha * (0.5)
            print(alpha)
            y = x + alpha*direction
            #print("y", y)
            phi_alpha = function(y, n, eps)
            #print("phi_alpha", phi_alpha)
            nf += 1
            #print("loop")
            print("scarto", phi_alpha - f - alpha*gamma*gradient_dir)
                
        
    return alpha, phi_alpha, nf


def linesearch(f, function, x, n, gamma, alpha, direction, gradient_dir, nf, eps) :
    
    alfa=1
	
    y=np.zeros(n)
    
    y = x + alfa*direction
    f_alfa = function(y, n, eps)
    nf = nf + 1
    
    while(f_alfa > (f + alfa*gamma*gradient_dir)):
        alfa = alfa/2
        y = x + alfa*direction
        f_alfa = function(y,n, eps)
        nf = nf + 1
        
        
    return alfa,f_alfa,nf

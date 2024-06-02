import numpy as np
from autograd import grad
from constants import *
from auxiliary import gradient_phi_dir, hessian, function
from problems import dim
from linesearch import linesearch_ArmijoNonMonotona, linesearch

def direction(f, nf, n, x, n_iter, eps) :
    eps_1 = 10**(-8)
    eps_2 = 10**(-3)
    p = np.zeros(n)
    s = -grad(function)(x, n, eps)
    nf += 1
    i = 0

    
    if np.dot(np.dot(s.T, hessian(x, n, s, eps)), s) < eps_1*(np.linalg.norm(s) ** 2) :
        return - grad(function)(x, n, eps)
    
    while i < MAX_ITER: 
        alpha = - np.dot(gradient_phi_dir(p, x, n, eps).T, s) / np.dot(np.dot(s.T, hessian(x, n, s, eps)), s)

        p = p + alpha*s
        
        if np.linalg.norm(gradient_phi_dir(p, x, n, eps)) <=  (eps_2 / (1 + n_iter)) * np.linalg.norm(grad(function)(x, n, eps)) :
            nf += 2
            return p
        
        i += 1
        
        beta = np.dot(np.dot(gradient_phi_dir(p, x, n, eps), hessian(x, n, s, eps)), s) / np.dot(np.dot(s.T, hessian(x, n, s, eps)), s)
        
        s = -gradient_phi_dir(p, x, n, eps) + beta*s
        nf += 1
        
        
        if np.dot(np.dot(s.T, hessian(x, n, s, eps)), s) < eps_1*(np.linalg.norm(s) ** 2) :
            return p
        
        
        if s.all() <= 10 ** (-8) : break
    
        #if np.linalg.norm(s) <= 10**(-8) : break
    
    return p
    
def troncatoMAIN(eps, delta, x0) :
    alpha = 10**(-3)
    gamma = 10**(-6)
    #if delta < 10**(-9) : delta = 10**(-9)
    #print(delta, "delta")
    n = dim()
    x = x0
    #Wtrhd = 10**(-5)

    n_iter = 0
    max_iter = 2**8 - 1
    f = function(x, n, eps)
    nf = 1
    l = []

    while True:
        norm_gradient = np.sqrt(np.dot(grad(function)(x, n, eps).T, grad(function)(x, n, eps)))
        #print(norm_gradient)
        #norm_gradient = np.sqrt(grad(function) * grad(function))
        #print("n_itert =",n_iter,"  nf =",nf,"f =",  f,"norma_grad =", norm_gradient)
        if norm_gradient <= delta:
            # print("\nAlgoritmo locale terminato con un punto stazionario, valore di funzione obiettivo:", function(x, n, eps), "\n")
            # for i in range(0, n) :
            #     print  ("\nx(",i+1,") =",x[i], "\n")
            break
            
        if n_iter > max_iter :
            # print("\nAlgoritmo terminato per massimo numero di iterazioni")
            # #print("\nNorma attuale del gradiente:", norm_gradient)
            # for i in range(0, n) :
            #     print  ("\nx(",i+1,") =",x[i], "\n")
            break
        
        direct = direction(f, nf, n, x, n_iter, eps)
        #print("direction", direct)
        #if np.linalg.norm(direct) <= 10**(-9) : break
        #gradient_dir = np.dot(grad(function).T, direct)
        gradient_dir = np.dot(grad(function)(x, n, eps).T, direct)
        #print("gradient_dir", gradient_dir)
    
        # alpha, phi_alpha, nf = linesearch_ArmijoNonMonotona(l, f, function, x, n, gamma, alpha, direct, gradient_dir, nf, eps)
        alpha, phi_alpha, nf = linesearch(f, function, x, n, gamma, alpha, direct, gradient_dir, nf, eps)

        #print("alpha", alpha, "phi_alpha", phi_alpha)
        x = x + alpha*direct
        #print("x", x)
        
        
        """
        ### DA CAMBIARE OGNI VOLTA ###
        if (x - 1000 > 0).any() :
            break
        if (x + 1000 < 0).any() :
            break
        """
        
        f = phi_alpha
        l.append(f)
        #print("f", f)
    
        n_iter += 1
        #print(n_iter)
        #print("------------------- fatta iterazione", n_iter, "-------------------")
        #print("\n")
    
    # print("Iterazioni del Troncato: ", n_iter)
    # print("Norma del gradiente: ", norm_gradient)

    return x
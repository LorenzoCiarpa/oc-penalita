import numpy as np
from autograd import grad, jacobian
from problems import P



def hessian(x, n, direct, eps):
    g = grad(function)
    return jacobian(g)(x, n, eps)

def gradient_phi_dir(d, x, n, eps) :
    gpd =  np.dot(hessian(x, n, d, eps), d) + grad(function)(x, n, eps)
    return gpd

def function(x, n, eps):
    return P(x, eps, n)

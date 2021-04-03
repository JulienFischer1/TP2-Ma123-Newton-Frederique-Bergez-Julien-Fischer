"""TP n°3 génie mathematique (Ma123) 
Julien Fischer, Frédérique Bergez""" 

import math

def f0(x): 
    return x+1
def fder0(x):
    return 1
def f1(x):
    return (x**4)+3*x-9
def fder1(x):
    return 4*(x**3)+3
def f1bis(x):
    return (x**4)+3*x-9
def fder1bis(x):
    return 4*(x**3)+3
def f2(x):
    return x-3*(math.cos(x))+2
def fder2(x):
    return 1+3*math.sin(x)
def f2bis(x):
    return x-3*(math.cos(x))+2
def fder2bis(x):
    return 1+3*math.sin(x)
def f2ter(x):
    return x-3*(math.cos(x))+2
def fder2ter(x):
    return 1+3*math.sin(x)
def f3(x):
    return x*(math.exp(x))-7
def fder3(x):
    return (1+x)*(math.exp(x))
def f4(x):
    return math.exp(x)-x-10
def fder4(x):
    return math.exp(x)-1
def f4bis(x):
    return math.exp(x)-x-10
def fder4bis(x):
    return math.exp(x)-1
def f5(x):
    return 2*math.tan(x)-x-5
def fder5(x):
    return (2/((math.cos(x))**2))-1
def f6(x):
    return math.exp(x)-(x**2)-3
def fder6(x):
    return math.exp(x)-2*x
def f7(x):
    return 3*x+4*math.log(x)-7
def fder7(x):
    return 3+(4/x)
def f8(x):
    return (x**4)-2*(x**2)+4*x-17
def fder8(x):
    return 4*(x**3)-4*x+4
def f8bis(x):
    return (x**4)-2*(x**2)+4*x-17
def fder8bis(x):
    return 4*(x**3)-4*x+4
def f9(x):
    return math.exp(x)-2*math.sin(x)-7
def fder9(x):
    return math.exp(x)-2*math.cos(x)
def f10(x):
    return math.log((x**2)+4)*math.exp(x)-10
def fder10(x):
    return math.exp(x)*math.log((x**2)+4)+((2*x)/((x**2)+4))

def Newton(f,fder,x0,epsilon,Nitermax):
    xold = x0
    xnew = xold-((f(xold))/(fder(xold)))
    erreur = xnew - xold
    n = 1
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold-((f(xold))/(fder(xold)))
        erreur = xnew - xold
        xold = xnew
        n += 1
        print(xnew,n,xnew - xold)
    return xnew

print("-----"*10)
print("solution de f0 (test) :")
Newton(f0, fder0,0,1e-4,1e4)
print("-----"*10)


print("solution de f1 :")
Newton(f1, fder1,3/2,1e-4,1e4)
print("-----"*10)

print("solution de f1bis :")
Newton(f1bis, fder1bis,-2,1e-4,1e4)
print("-----"*10)

print("solution de f2 :")
Newton(f2, fder2,0.54,1e-4,1e4)
print("-----"*10)

print("solution de f2bis :")
Newton(f2bis, fder2bis,-1.4,1e-4,1e4)
print("-----"*10)

print("solution de f2ter :")
Newton(f2ter, fder2ter,-3.5,1e-4,1e4)
print("-----"*10)

print("solution de f3 :")
Newton(f3, fder3,1.4,1e-4,1e4)
print("-----"*10)

print("solution de f4 :")
Newton(f4, fder4,2.5,1e-4,1e4)
print("-----"*10)

print("solution de f4bis :")
Newton(f4bis, fder4bis,-10.3,1e-4,1e4)
print("-----"*10)

print("solution de f5 :")
Newton(f5, fder5,1.5,1e-4,1e4)
print("-----"*10)

print("solution de f6 :")
Newton(f6, fder6,1.8,1e-4,1e4)
print("-----"*10)

print("solution de f7 :")
Newton(f7, fder7,1.4,1e-4,1e4)
print("-----"*10)

print("solution de f8 :")
Newton(f8, fder8,2,1e-4,1e4)
print("-----"*10)

print("solution de f8bis :")
Newton(f8bis, fder8bis,-2.8,1e-4,1e4)
print("-----"*10)

print("solution de f9 :")
Newton(f9, fder9,2,1e-4,1e4)
print("-----"*10)

print("solution de f10 :")
Newton(f10, fder10,0,1e-4,1e4)
print("-----"*10)
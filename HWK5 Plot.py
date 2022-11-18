# -*- coding: utf-8 -*-
"""
@author: Chris George
HWK5 Plot
"""
from matplotlib import pyplot as plt 
import numpy as np

D = 7.31e-19
B = 1.81e10
k=2*D*B**2

x = np.arange(-100e-12,300e-12,1e-15)

BO = B*x*-1
#Morse
def f1(x):
    return (D)*(1-np.exp(BO))**2

#harmonic
def f2(x):
    return 0.5*k* x**2


plt.plot(x,f1(x),'r',label='Morse potential')
plt.plot(x,f2(x),'b',label='harmonic potential')
plt.xlabel("x / pm")
plt.ylabel("v(x) /10^-18 J")
plt.title('Potentials')
#plt.xlim([-100, 300])
plt.ylim([0,1.5e-18])

plt.legend()
plt.show()
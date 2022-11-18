# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 00:56:26 2022

@author: Chris George
"""
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

#Question 6-22 plot

#From Table 6.2
#=============#

#observed frequencies of H35Cl in cm^-1
w = [83.03,104.10,124.30,145.03,165.51,185.86,206.38,226.50]

#J+1
j = [4,5,6,7,8,9,10,11]

#(J+1)^2
j2 = [i**2 for i in j]

#v/(J+1)
r = [i/j for i,j in zip(w,j)]

plt.scatter(j2,r)
z = np.polyfit(j2, r, 1)
t = np.poly1d(z)
plt.plot(j2, t(j2), color="red",linewidth=1.5, linestyle="--")
plt.xlabel('(J+1)\u00b2')
plt.ylabel('v/(J+1) in cm\u207b\u00b9')
plt.title('Trendline to find B̃ and Ď')
plt.show()

print(f'Equation of trendline (from numpy):{t}\n')
m = round(z[0],5)
b = round(z[1],2)
print(f'The slope is {m}')
print(f'ASnd the y-int is {b}\n')
Ď = -m/4
B̃ = b/2
print(f'Ď = {Ď} cm\u207b\u00b9')
print(f'B̃ = {B̃} cm\u207b\u00b9')

#Question 6-45 plot

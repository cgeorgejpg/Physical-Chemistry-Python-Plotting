# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:43:33 2022

@author: Chris C. George

This code was used for both problems 5-18 and 5-40.
"""
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

#for 5-18.

#v values
v = [1,2,3,4,5]
print("\u03BD:")
print(v)
print("\n")
#frequencies
fre = [381.20, 759.60, 1135.00, 1507.40 , 1877.00]
print("\u03C9:")
print(fre)
print("\n")
#v+1 values
vn = [i+1 for i in v]
print("\u03BD+1:")
print(vn)
print("\n")
#list of frequencies/v
frea = [i / j for i,j in zip(fre, v)]
print("\u03C9_obs/\u03BD")
print(frea)
print("\n \n")
#graph of frea vs. vn                                                                                    
plt.plot(vn,frea)  
plt.title('\u03C9_obs/\u03BD versus \u03BD +1')
plt.ylabel('\u03C9_obs/\u03BD')
plt.xlabel('\u03BD +1')
plt.show()
#numerical answers
slope, intercept = np.polyfit(vn,frea,1)
print(f"(slope): {slope}")
s = -round(slope,3)
print(f"(y-intercept): {intercept} \n \n")
i = round(intercept,2)
print(f"==>\nx\u03C9 = {s}cm^-1 \n\u03C9 = {i}cm^-1")

#for 5-40.
j = np.arange(0, 5, 0.1)
w = 1000
k_B = 0.695038
T = 300
#e = -j*w/(k_B*T)
f_j = np.exp(-j*w/(k_B*T))
plt.plot(j,f_j)
plt.title('Vibrational States at t=300K')
plt.ylabel('f_j')
plt.xlabel('j')
plt.show()
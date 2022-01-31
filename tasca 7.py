# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:01:54 2022

@author: guill
""" 

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt




N = 2000 # mostres 
L = 1 # longitud en segons 
t = np.linspace(0, L, N)
T = L/N
ft = 1/2/T  # Teorema de Shanon
frequencia_1 = 5 # Hz

Funcio_g = signal.square(frequencia_1 * 2 * np.pi * t, 0.5)
Funcio_h = signal.sawtooth(frequencia_1 * 2 * np.pi * t, 0.5)
Transformada_g = np.fft.fft(Funcio_g)
Transformada_h = np.fft.fft(Funcio_h)

plt.figure()
plt.subplot(211)
plt.plot(t, Funcio_g) 
plt.plot(t, Funcio_h) 

plt.subplot(212)
plt.plot(t, np.abs(Transformada_g)) # frequencia en Hz 
plt.plot(t, np.abs(Transformada_h)) # frequencia en Hz 
plt.show()
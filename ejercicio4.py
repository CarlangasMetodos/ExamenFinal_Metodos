#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

#a
plt.figure()
plt.plot(y,t)
plt.savefig('senal.png')

#b
fourier=[]

def fourier(y):
    for i in range(N):
        e=np.exp(2.0*np.pi*t*i*n/N)
        fourier.append(np.sum(y[i]*e))
        
    return fourier

norm_f=fft(fourier(y))/n

plt.figure()
plt.plot(norm_f,t)
plt.savefig('fourier.png')

#c
for i in range(len(fourier)):
   if(fourier[i]>=10000):
        fourier[i]=0

plt.figure()
plt.plot(fourier,t)
plt.savefig('filtro.png')
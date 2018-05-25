# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

#Calcula derivadas
derivada1=[]
derivada2=[]

h=2.0/10 #Porque x va de 0 a 2 y tiene 10 puntos

derivada1.append((fx[:-1]-fx[:-1])/h)
derivada2.append((derivada1[:-2]-derivada1[:-1])/h)

#Grafica la funcion
plt.figure()
plt.plot(x,derivada2)
plt.savefig('segunda.png')

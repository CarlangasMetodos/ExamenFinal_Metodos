#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

#Calcula covarianza
meanu=np.mean(u)
meanv=np.mean(v)

uu=[]
vv=[]
valu=0
valv=0
valor=0

for i in range (len(u)):
    valu=u[i]-meanu
    valv=v[i]-meanv    
    uu.append(valu)
    vv.append(valv)
    valor+=uu[i]*vv[i]

covarianza=valor/(len(t)-1)
print (covarianza)
    
#Grafica de datos

plt.figure()
plt.title('Serie')
plt.plot(u,t, label='u', c='r')
plt.plot(v,t, label='v', c='b')
plt.legend()
plt.savefig('serie.png')

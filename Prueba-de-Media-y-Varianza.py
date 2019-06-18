import matplotlib.pyplot as plt
import random
import math

ntr=int(input("CUANTOS NUMEROS ALEATORIOS QUIERES: "))
lista=[]
listamedia=[]
temporal=0
suma=0

for i in range(ntr):
    numeros=random.random()
    lista.append(numeros)
    temporal=numeros+temporal

media=(temporal/ntr)

Li=(0.5-(1.96/math.sqrt(12*ntr)))
Ls=(0.5+(1.96/math.sqrt(12*ntr)))
print('LA MEDIA ES:',media)
print('EL LIMITE INFERIOR ES:',Li)
print('EL LIMITE SUPERIOR ES:',Ls)

if (media>=Li or media<=Ls):
    print("SE ACEPTA LA HIPOTESIS PARA LA MEDIA")
else:
    print("SE RECHAZA LA HIPOTESIS PARA LA VARIANZA")

plt.plot(lista)
plt.ylabel('LOS NUMEROS RANDON SON')
plt.show()

for i in range(ntr):
    listamedia.append(media)

mediavarianza=[(x1-x2)**2 for (x1,x2)in zip (lista,listamedia)]

for l in mediavarianza:
    suma=suma+l

varianza=(suma/(ntr-1))

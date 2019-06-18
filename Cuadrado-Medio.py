import matplotlib.pyplot as plt

semilla=int(input("PONGA LA SEMILLA: "))
ntr=int(input("CUANTOS NUMEROS ALEATORIOS QUIERES: "))
lista=[]

for i in range(ntr):
    cuadrado=str(semilla**2)
    inicio= int(len(cuadrado)/2)-2
    fin= int(len(cuadrado)/2)+2
    print (cuadrado[inicio:fin])
    semilla=int(cuadrado[inicio:fin])
    pseudoaleatorio=float('0.'+str(semilla))
    print (pseudoaleatorio)
    lista.append(pseudoaleatorio)

print (lista)
plt.plot(lista)
plt.ylabel('ESTOS SON LOS NUEMOS RANDON')
plt.show()
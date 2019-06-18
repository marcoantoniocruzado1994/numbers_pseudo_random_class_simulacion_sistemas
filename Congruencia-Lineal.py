import matplotlib.pyplot as plt

semilla=int(input("PONGA LA SEMILLA: "))
a=int(input("Ingrese el multiplicador  de constante 'A': "))
c=int(input("Ingrese el incremento 'C': "))
m=int(input("Ingrese el modulo 'M': "))
ntr=int(input("CUANTOS NUMEROS ALEATORIOS QUIERES: "))
lista=[]

for i in range(ntr):
    R=((a*semilla + c)%m)
    print (R)
    pseudoaleatorio=(R/m)
    lista.append(pseudoaleatorio)
    semilla=R

print (lista)
plt.plot(lista)
plt.ylabel('ESTOS SON LOS NUEMOS RANDON')
plt.show()
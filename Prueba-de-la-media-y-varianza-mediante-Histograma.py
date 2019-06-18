#!/usr/bin/env python
import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Funcion para generar aleatorios
def listaAleatorios(n):
    lista = [0] * n

    for i in range(n):
        lista[i] = random.randint(0, 100)

    return lista


# Imprime los valores aleatorios generados
def imprimirTabla(aleatorios):
    x = PrettyTable()

    x.field_names = ["Numero", "Valor"]

    count = 1
    for i in aleatorios:
        x.add_row([count, i])
        count += 1

    print(x)

    return


def calcularMedia(aleatorios):
    media = 0
    suma = 0
    len_nums = len(aleatorios)

    for i in aleatorios:
        suma += i

    media = suma / len_nums

    return media


def calcularVarianza(lista):
    s = 0
    m = calcularMedia(lista)

    for elemento in lista:
        s += (elemento - m) ** 2

    return s / float(len(lista))

def graficarMedia(aleatorios):
    plt.plot(aleatorios)
    plt.show()

    return

def graficarVarianza(aleatorios):
    plt.hist(aleatorios, 40)
    plt.show()

    return



if __name__ == "__main__":
    print("CUANTOS NUMEROS ALEATORIOS QUIERES (0 - 100): ")
    n = int(input())

    print("\n")

    aleatorios = listaAleatorios(n)

    imprimirTabla(aleatorios)

    print("\n")

    print("Calculo de MEDIA =", calcularMedia(aleatorios))
    print("\n")

    print("Calculo de la VARIANZA =", calcularVarianza(aleatorios))
    print("\n")

    print("GRAFICO DE LA MEDIA")
    graficarMedia(aleatorios)

    print("\n")

    print("GRAFICO DE LA VARIZANZA")
    graficarVarianza(aleatorios)
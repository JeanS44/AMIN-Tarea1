import sys
import numpy as np
import math

if len(sys.argv) == 4 :
    semilla = int(sys.argv[1])
    tamanoTableros = int(sys.argv[2])
    cantidadTableros = int(sys.argv[3])
    print("semilla: ", semilla, " Tamaño del tablero: ", tamanoTableros, " Cantidad de tableros: ", cantidadTableros)
else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tamaño de tablero' 'Cantidad de tableros'")
    sys.exit(0)

np.random.seed(semilla)

poblacionInicial = np.zeros((cantidadTableros, tamanoTableros), int)

for i in range(cantidadTableros):
    poblacionInicial[i] = np.arange(0, tamanoTableros)
    np.random.shuffle(poblacionInicial[i])

print(poblacionInicial)

maximoAtaques = tamanoTableros*(tamanoTableros-1)/2
choquesDiagonales = np.zeros((cantidadTableros), float)

for tablero in range(len(poblacionInicial)):
    for i in range(len(poblacionInicial[tablero])):
        arrayAux = poblacionInicial[tablero]
        for j in range(len(poblacionInicial[tablero])):
            if abs(i-j) == abs(poblacionInicial[tablero][i] - poblacionInicial[tablero][j]) and i != j:
                choquesDiagonales[tablero] +=1
                """ print("Tablero N°: ",tablero ,
                " Donde fila", i, " Valor ", poblacionInicial[tablero][i],
                " Donde fila", j, " Valor ", poblacionInicial[tablero][j],
                "La resta de iteradores es: ", abs(i-j),
                "La resta de resultados es: ", abs(poblacionInicial[tablero][i] - poblacionInicial[tablero][j])) """

suma_total = 0

for i in range(len(choquesDiagonales)):
    choquesDiagonales[i] = maximoAtaques - choquesDiagonales[i]
    suma_total = np.sum(choquesDiagonales)
    print(choquesDiagonales)
    print("xd", suma_total)
    choquesDiagonales[i] /= suma_total
    choquesDiagonales[i] = round(choquesDiagonales[i],2)
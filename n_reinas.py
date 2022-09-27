# -*- coding: UTF-8 -*-
import sys
import numpy as np
import math

def inicializarPoblacion(tamano, cantidad):
    poblacionInicial = np.zeros((cantidad, tamano), int)
    for i in range(cantidadTableros):
        poblacionInicial[i] = np.arange(0, tamanoTableros)
        np.random.shuffle(poblacionInicial[i])
    return poblacionInicial

def determinarFitness(poblacionInicial, cantidad, tamano):
    arrayFitness = np.zeros(cantidad, float)
    for tablero in range(len(poblacionInicial)):
        for i in range(len(poblacionInicial[tablero])):
            for j in range(len(poblacionInicial[tablero])):
                if abs(i-j) == abs(poblacionInicial[tablero][i] - poblacionInicial[tablero][j]) and i != j:
                    arrayFitness[tablero] += 1
        arrayFitness[tablero] /= 2
    np.append(arrayFitness, (tamano*(tamano-1)/2)-arrayFitness[tablero])
    return arrayFitness

def determinarSumaTotal(fitness):
    return np.sum(fitness)

def determinarProporcion(fitness):
    sumatotal = np.sum(fitness)
    for i in range(len(fitness)):
        fitness[i] = (fitness[i])/sumatotal
        fitness[i] = round(fitness[i],6)
    return fitness

def determinarProporcion(fitness):
    sumatotal = np.sum(fitness)
    for i in range(len(fitness)):
        fitness[i] = (fitness[i])/sumatotal
        fitness[i] = round(fitness[i],6)
    return fitness

def determinarRuleta(fitness):
    ruleta = np.array([])
    ruleta = np.append(ruleta, fitness[0]/np.sum(fitness))
    for i in range(1, len(fitness)):
        proporcion = fitness[i]/np.sum(fitness)
        ruleta = np.append(ruleta, ruleta[i-1]+proporcion)
    return ruleta

if len(sys.argv) == 4:
    semilla = int(sys.argv[1])
    np.random.seed(semilla)
    tamanoTableros = int(sys.argv[2])
    cantidadTableros = int(sys.argv[3])
    poblacion = inicializarPoblacion(tamanoTableros, cantidadTableros)
    print(poblacion)
    fitness = determinarFitness(poblacion, cantidadTableros, tamanoTableros)
    print(fitness)
    suma_total = determinarSumaTotal(fitness)
    print(suma_total)
    proporcion = determinarProporcion(fitness)
    print(proporcion)
    ruleta = determinarRuleta(fitness)
    print(ruleta)
else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tamaño de tablero' 'Cantidad de tableros'")
    sys.exit(0)
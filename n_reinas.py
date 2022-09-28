# -*- coding: UTF-8 -*-
import sys
import numpy as np
import random

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

def determinarRuleta(fitness):
    ruleta = np.array([])
    ruleta = np.append(ruleta, fitness[0:1]/np.sum(fitness))
    for i in range(1, len(fitness)):
        proporcion = fitness[i]/np.sum(fitness)
        ruleta = np.append(ruleta, ruleta[i-1]+proporcion)
    return ruleta

def invertirFitness(fitness, tamano):
    fitness_invertido = np.array([])
    for i in range(len(fitness)):
        fitness_invertido = np.append(fitness_invertido, (tamano*(tamano-1)/2)-fitness[i])
    return fitness_invertido

def proporcionInvertida(fitnessInvertido):
    proporcion_invertida = np.array([])
    suma_fitness_invertido = np.sum(fitnessInvertido)
    for i in range(len(fitnessInvertido)):
        proporcion_invertida = np.append(proporcion_invertida, fitnessInvertido[i]/suma_fitness_invertido)
    return proporcion_invertida

def ruletaInvertida(fitnessInvertido):
    ruleta_ivertida = np.array([])
    ruleta_ivertida = np.append(ruleta_ivertida, fitnessInvertido[0]/np.sum(fitnessInvertido))
    for i in range(1, len(fitnessInvertido)):
        proporcion = fitnessInvertido[i]/np.sum(fitnessInvertido)
        ruleta_ivertida = np.append(ruleta_ivertida, ruleta_ivertida[i-1]+proporcion)
    return ruleta_ivertida

def seleccionIndividuos(ruleta_invertida):
    pos = 0
    azar = random.uniform(0, 1)
    for i in range(len(ruleta_invertida)):
        if azar <= ruleta_invertida[i]:
            pos=i
            #return pos, azar, ruleta_invertida[pos]
            return pos

def cruza(padre_1, padre_2):
    punto = random.randint(1, len(padre_1)-2)
    print("punto: "+str(punto))
    hijo_1, hijo_2 = padre_1.copy(), padre_2.copy()
    hijo_1 = np.append(padre_1[:punto], padre_2[punto:])
    hijo_2 = np.append(padre_2[:punto], padre_1[punto:])
    return [hijo_1, hijo_2]

def mutacion(individuo):
    return np.random.permutation(individuo)

if len(sys.argv) == 4:
    semilla = int(sys.argv[1])
    np.random.seed(semilla)
    tamanoTableros = int(sys.argv[2])
    cantidadTableros = int(sys.argv[3])
    iteraciones = 1
    poblacion = inicializarPoblacion(tamanoTableros, cantidadTableros)
    print(poblacion)

    #for i in range iteraciones:
    fitness = determinarFitness(poblacion, cantidadTableros, tamanoTableros)
    print("fitness: "+str(fitness))
    suma_total = determinarSumaTotal(fitness)
    print(suma_total)
    proporcion = determinarProporcion(fitness)
    print(proporcion)
    ruleta = determinarRuleta(fitness)
    print(ruleta)
    fitness_aux = determinarFitness(poblacion, cantidadTableros, tamanoTableros)
    fitness_invertido = invertirFitness(fitness_aux, tamanoTableros)
    print(fitness_invertido)
    proporcion_invertida = proporcionInvertida(fitness_invertido)
    print(proporcion_invertida)
    ruleta_invertida = ruletaInvertida(fitness_invertido)
    print(ruleta_invertida)
    print("----")
    seleccion = seleccionIndividuos(ruleta_invertida)
    print(seleccion)
    print(cruza(poblacion[seleccionIndividuos(ruleta_invertida)],poblacion[seleccionIndividuos(ruleta_invertida)]))
    if random.uniform(0,1) <= 0.05:
        print(mutacion(poblacion[seleccionIndividuos(ruleta_invertida)]))

else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tamaño de tablero' 'Cantidad de tableros'")
    sys.exit(0)
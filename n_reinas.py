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

def solucionFitness(tamano):
    return tamano*(tamano-1)/2

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
    punto = random.randint(0, len(padre_1)-1)
    hijo_1, hijo_2 = padre_1.copy(), padre_2.copy()
    hijo_1 = np.append(padre_1[:punto], padre_2[punto:])
    hijo_2 = np.append(padre_2[:punto], padre_1[punto:])
    return [hijo_1, hijo_2]

def rectificar(hijos):
    for i in range(len(hijos)):
        while(len(np.unique(hijos[i])) != len(hijos[i])):
            j = 0
            while(j < len(hijos[i])):
                if j not in hijos[i]:
                    u, c = np.unique(hijos[i], return_counts=True)
                    aux = 0
                    for k in range(len(hijos[i])):
                        if u[c>1][0] == hijos[i][k]:
                            aux = k
                    hijos[i][aux] = j
                    j = 0
                else:
                    j+=1
    return hijos

def mutacion(individuo):
    return np.random.permutation(individuo)

if len(sys.argv) == 7:
    semilla = int(sys.argv[1])
    if semilla>=0:
        np.random.seed(semilla)
    else:
        semilla = np.random.seed()
    tamanoTableros = int(sys.argv[2])
    cantidadTableros = int(sys.argv[3])
    iteracion = int(sys.argv[4])
    prob_cruza = float(sys.argv[5])
    prob_mutacion = float(sys.argv[6])
    poblacion = inicializarPoblacion(tamanoTableros, cantidadTableros)
    print(poblacion)

    for i in range(iteracion):
        print("----------------iteracion: ",str(i),"------------------------------------------------------")
        fitness_aux = determinarFitness(poblacion, cantidadTableros, tamanoTableros)
        fitness_invertido = invertirFitness(fitness_aux, tamanoTableros)
        print("fitness invertido: ",str(fitness_invertido))
        ruleta_invertida = ruletaInvertida(fitness_invertido)
        print("ruleta invertida: ",str(ruleta_invertida))
        
        print("----")

        poblacion_hijos = []
        indice = 0
        while(indice < len(poblacion)):
            
            padre_1, padre_2 = seleccionIndividuos(ruleta_invertida), seleccionIndividuos(ruleta_invertida)

            if np.array_equal(poblacion[padre_1],poblacion[padre_2]):
                pass
            else:
                if len(poblacion)-indice != 1:
                    if random.uniform(0,1) <= prob_cruza:
                        resultado_cruza = cruza(poblacion[padre_1],poblacion[padre_2])
                        if len(np.unique(resultado_cruza[0])) != len(resultado_cruza[0]):
                            resultado_cruza = rectificar(resultado_cruza)
                        print("resultado cruza doble: ",str(resultado_cruza))
                        poblacion_hijos.append(resultado_cruza[0])
                        poblacion_hijos.append(resultado_cruza[1])
                        indice+=2
                else:
                    if random.uniform(0,1) <= prob_cruza:
                        resultado_cruza = cruza(poblacion[padre_1],poblacion[padre_2])
                        if len(np.unique(resultado_cruza[0])) != len(resultado_cruza[0]):
                            resultado_cruza = rectificar(resultado_cruza)
                        print("resultado cruza single: ",str(resultado_cruza))
                        poblacion_hijos.append(resultado_cruza[random.randint(0,1)])
                        indice+=1

                if random.uniform(0,1) <= prob_mutacion and len(poblacion_hijos)!=0:
                    poblacion_hijos[indice-1] = mutacion(poblacion_hijos[indice-1])

        poblacion = np.array(poblacion_hijos)
        print(poblacion)

    fitness_aux = determinarFitness(poblacion, cantidadTableros, tamanoTableros)
    for n in range(len(fitness_aux)):
        if fitness_aux[n] == 0:
            print(str(n)," - ",str(poblacion[n]))

else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tamaño de tablero' 'Cantidad de tableros' 'Iteraciones' 'Probabilidad Cruza' 'Probabilidad Mutacion' ")
    sys.exit(0)
#
# DESCRIPCIÓN:
# Implementación de un Multi-Layer Perceptron con 1 capa oculta utilizando
# función sigmoide para la activación de neuronas en la capa oculta y de
# salida y entrenamiento mediante el algoritmo de BackPropagation (BP)
#
# Creado el 04/06/2019
# Inteligencia Artificial II - Ingeniería en Mecatronica
# Facultad de Ingeniería - Universidad Nacional de Cuyo
# Autor: Sebastian Giunta, P8 capo, Ichmew
#

import math
import matplotlib
import numpy as np
from datataset import genera_data
from datataset import dataset_size

# Definición de hiperparámetros de la red
NEURONAS_ENTRADA = 4
NEURONAS_CAPA_OCULTA = 15
NEURONAS_SALIDA = 4
PORCENTAJE_EJEMPLOS_TEST = 5.0
EPSILON = 0.4
EJEMPLOS_CANT = dataset_size()
EJEMPLOS_TEST = int(dataset_size() * 0.1)
EPOCHS = 10000
CANTIDAD_ENTRADAS_SALIDAS = 1  # depende del dataset, es para el t
mostrar_e_s = 1


# Función de activación Heavyside de la capa de entrada
def Heavy(x):
    if x >= 0:
        return 1
    else:
        return 0


# Función de activación sigmoide de la capa de entrada
def f(x):
    return 1 / 1 + math.exp(-x)


# Derivada de la función de activación de la capa de entrada
def f_derivada(x):
    return math.exp(-x) / ((1 + math.exp(-x)) * (1 + math.exp(-x)))


# Función de activación de la capa oculta
def g(x):
    return x


# Derivada de la función de activación de la capa oculta
def g_derivada(x):
    return 1


# Cálculo de las salidas de cada capa y de las salidas finales
Wji = np.zeros[NEURONAS_ENTRADA, NEURONAS_CAPA_OCULTA]
Wkj = np.zeros[NEURONAS_CAPA_OCULTA, NEURONAS_SALIDA]
x = np.zeros(NEURONAS_ENTRADA)
y = np.zeros(NEURONAS_CAPA_OCULTA)
z = np.zeros(NEURONAS_SALIDA)
cant_ej_training = EJEMPLOS_CANT - EJEMPLOS_TEST
tasa_aciertos = 0


def calculo_salidas(Wji, Wkj, x, y, z):
    # Se encarga de calcular la salida z de cada neurona

    # Cálculo de salidas de la capa oculta
    for j in range(0, NEURONAS_CAPA_OCULTA):
        entrada_y = 0
        for i in range(0, NEURONAS_ENTRADA):
            entrada_y += Wji[i][j] * x[i]
        # Sesgo de las neuronas de la capa oculta
        entrada_y -= Wji[NEURONAS_ENTRADA - 1][j]
        # Valor de salida de la neurona j
        y[j] = f(entrada_y)

    # Cálculo de salidas de la capa de salida
    for k in range(0, NEURONAS_SALIDA):
        entrada_z = 0
        for j in range(0, NEURONAS_CAPA_OCULTA):
            entrada_z = Wkj[j][k] * y[j]
        # Sesgo de las neuronas de la cada de salida
        entrada_z -= Wkj[NEURONAS_CAPA_OCULTA - 1][k]
        # Valor de salidad de la neurona k
        z[k] = g(entrada_z)


def bp(Wji, Wjk, x, y, z, t):
    # Se encarga de actualizar los pesos sinápticos

    delta_mu_k = []
    # Actualización pesos capa oculta-capa salida
    for k in range(0, NEURONAS_SALIDA):
        h_mu_k = 0
        for j in range(0, NEURONAS_CAPA_OCULTA):
            h_mu_k += Wkj[j][k] * y[j]
        h_mu_k -= Wkj[NEURONAS_CAPA_OCULTA][k]
        delta_mu_k[k] = (t[k] - g(h_mu_k)) * g_derivada(h_mu_k)
        for j in range(0, NEURONAS_CAPA_OCULTA):
            Wkj[j][k] += EPSILON * delta_mu_k[k] * y[j]

        Wkj[NEURONAS_CAPA_OCULTA][k] += EPSILON * delta_mu_k[k] * -1
    # Actualización pesos capa entrada-capa oculta
    for j in range(0, NEURONAS_CAPA_OCULTA):
        h_mu_j = 0
        for i in range(0, NEURONAS_ENTRADA):
            h_mu_j += Wji[i][j] * x[i]
        h_mu_j -= Wji[NEURONAS_ENTRADA][j]
        delta_mu_j = 0
        for k in range(0, NEURONAS_SALIDA):
            delta_mu_j += delta_mu_k[k] * Wkj[j][k]
        delta_mu_j *= f_derivada(h_mu_j)
        for i in range(0, NEURONAS_ENTRADA):
            Wji[i][j] += EPSILON * delta_mu_j * x[i]
        Wji[NEURONAS_ENTRADA][j] += EPSILON * delta_mu_j * -1

'''
def calcula_LMS(ejemplos, Wji, Wkj, EJEMPLOS_CANT):
    # Se encarga del validation??

    # ejemplos es la matriz de las dataset de donde sacamos las entradas
    # y EJEMPLOS_CANT es la cantidad todal de ejemplos
    cant_ej_test = int(PORCENTAJE_EJEMPLOS_TEST / 100.0) * EJEMPLOS_CANT
    cant_ej_training = EJEMPLOS_CANT - cant_ej_test

    error_2 = 0
    for mu in range(cant_ej_training, EJEMPLOS_CANT):
        # Probamos el rendimiento de la red en los ejemplos del dataset que
        # estan A PARTIR del ultimo ejemplo de entrenamiento
        for i in range(0, NEURONAS_ENTRADA):
            x[i] = ejemplos[mu][i]

        # Calcular salida de la red
        calculo_salidas(Wji, Wkj, x, y, z)

        # Vector de salidas deseada
        t[int(ejemplos[mu][CANTIDAD_ENTRADAS_SALIDAS - 1])] = 1

        for k in range(0, NEURONAS_SALIDA):
            error_2 += pow(t[k] - z[k], 2)

    error_2_medio = error_2 / (cant_ej_test)  # Falta dividir por 2??

    return error_2_medio'''


def calcula_rendimiento(ejemplos, Wji, Wkj, mostrar_e_s):
    # Se encarga de calcular la tasa de aciertos de cada epoch

    aciertos = 0
    ejemplo = 0
    for mu in range(0, cant_ej_training):
        for i in range(0, NEURONAS_ENTRADA):
            x[i] = ejemplos[mu][i]
        calculo_salidas(Wji, Wkj, x, y, z)
        # Si usamos sólo una neurona, saltamos directamente (es necesario
        # comentar lo que están en el medio) a la verificación de errores.
        # Utilizamos para ello el z de calculo_salidas y el t del dataset.
        max = z[0]
        for k in range(1, NEURONAS_SALIDA):
            if max < z[k]:
                max = z[k]
        for k in range(0, NEURONAS_SALIDA):
            if max != z[k]:
                z[k] = 0
            else:
                z[k] = 1.0
        t = np.zeros(NEURONAS_SALIDA)
        t[int(salida[mu])] = 1
        # Verificación de aciertos
        error = 0
        if mostrar_e_s == 1:
            print(str((ejemplo + 1)), '. z=[')
        for k in range(0, NEURONAS_SALIDA):
            error += round(pow(pow(t[k] - z[k], 2), 0.5))
            if mostrar_e_s == 1:
                print(str(z[k]))
        if mostrar_e_s == 1:
            print('] -- t=[')
            for k in range(0, NEURONAS_SALIDA):
                print(str(t[k]))
            print(']\n')
            ejemplo = ejemplo + 1
        if error == 0:
            aciertos = aciertos + 1
    # Calculamos la tasa de aciertos
    tasa_aciertos = aciertos / cant_ej_training


def calcula_final(ejemplos, Wji, Wkj, cant_total_ej, mostrar_e_s):
    cant_ej_test = int(PORCENTAJE_EJEMPLOS_TEST / 100.0 * cant_total_ej)
    cant_ej_training = cant_total_ej - cant_ej_test
    # Prueba del rendimiento con TEST
    aciertos = 0
    ejemplo = 0
    for mu in range(cant_ej_training, cant_total_ej):
        for i in range(0, NEURONAS_ENTRADA):
            x[i] = ejemplos[mu][i]
        calculo_salidas(Wji, Wkj, x, y, z)
        # Si usamos sólo una neurona, saltamos directamente (es necesario
        # comentar lo que están en el medio) a la verificación de errores.
        # Utilizamos para ello el z de calculo_salidas y el t del dataset.
        max = z[0]
        for k in range(1, NEURONAS_SALIDA):
            if max < z[k]:
                max = z[k]
        for k in range(0, NEURONAS_SALIDA):
            if max != z[k]:
                z[k] = 0
            else:
                z[k] = 1.0
        t = np.zeros(NEURONAS_SALIDA)
        t[int(ejemplos[mu][NEURONAS_SALIDA - 1])] = 1
        # Verificación de aciertos
        error = 0
        if mostrar_e_s == 1:
            print(str((ejemplo + 1)), '. z=[')
        for k in range(0, NEURONAS_SALIDA):
            error += round(pow(pow(t[k] - z[k], 2), 0.5))
            if mostrar_e_s == 1:
                print(str(z[k]))
        if mostrar_e_s == 1:
            print('] -- t=[')
            for k in range(0, NEURONAS_SALIDA):
                print(str(t[k]))
            print(']\n')
            ejemplo = ejemplo + 1
        if error == 0:
            aciertos = aciertos + 1
    # Calculamos la tasa de aciertos
    tasa_aciertos = aciertos / cant_ej_test

# def genera_dataset(x, t):


# MAIN ------------------------------------------------------------------------
t = np.zeros[EJEMPLOS_CANT, NEURONAS_SALIDA]
Wji = np.random.rand(NEURONAS_ENTRADA, NEURONAS_CAPA_OCULTA)
Wkj = np.random.rand(NEURONAS_CAPA_OCULTA, NEURONAS_SALIDA)

dataset_t, ejemplos = genera_data()


for e in range(0, EPOCHS):
    # TRAINING
    for mu in range(0, EJEMPLOS_CANT - EJEMPLOS_TEST):
        x = ejemplos[mu][:]
        t = dataset_t[mu][:]
        calculo_salidas(Wji, Wkj, x, y, z)
        bp(Wji, Wkj, x, y, z, t)
    calcula_rendimiento(ejemplos, Wji, Wkj, mostrar_e_s)
    print('Epoch ', e, ': ', tasa_aciertos, '\n')

# waiting = input()
# TEST / VALIDATION
error = 0
'''for mu in range(EJEMPLOS_CANT - EJEMPLOS_TEST, EJEMPLOS_CANT):
    calculo_salidas(Wji, Wkj, x[mu], y, z)
    error +=

# print('\nTest final:')'''


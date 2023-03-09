import random
import math

# TODO: funcion para ingresar a los datos de inversion 
# Funcion para pasar de decimal a binario y validar que la suma de cada cromosoma sea 10 
# [0.875 0.875 0.875 0.875] - 0.875 - es el mas optimo 
# max f(x)

def binario_a_decimal(cromosoma):
    valid = False
    numeros_decimal = [] 
    print(cromosoma)
    i = 0
    while(True):
        numeros_decimal.append(cromosoma[i:i+3])
        if(i == len(cromosoma)-3):
            break
        i = i+3
    print(numeros_decimal)
    return valid

def crear_poblacion(num_cromo, num_gen): 
    poblacion = []
    cromosoma = []
    for i in range(1): 
        for j in range(12):
            cromosoma.append(random.randint(0,1))
        binario_a_decimal(cromosoma)
        poblacion.append(cromosoma)
        cromosoma = []
    return poblacion

def resultados_evaluacion(resultados,resultado, tienda):
    resultados = {}
    for i in range(tienda):
        resultados[i] = [resultado] 

def funcion_objetivo(x): 
    result = (1-((11/2*x)-7/2)^2)*(math.cos(((11/2*x)-7/2))+1)+2
    return result

def main(num_cromo, num_gen): 
    poblacion_inicial = crear_poblacion(num_cromo=num_cromo, num_gen=num_gen)
    for i in range(num_cromo):
        print(poblacion_inicial[i])
    
crear_poblacion(1,12)
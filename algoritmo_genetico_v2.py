'''
c) De cada par de padres y de par de hijos, elegir los dos
mejores y devolverlos a la posición que tenían los padres
de ese cruzamiento

d) Realizarlo hasta 250 generaciones o cuando encuentre
el primer individuo con 10 ceros.

'''

import random
import argparse

#recibe 4 cromosomas madre, padre, hijo1, hijo2
def elegirMejores(*args): 
    cromosoma_mejor_1 = []
    cromosoma_mejor_2 = []
    ordenado = sorted(args, key=lambda x: x.count('0'), reverse=True)
    cromosoma_mejor_1 = ordenado[0]
    cromosoma_mejor_2 = ordenado[1]
    return cromosoma_mejor_1, cromosoma_mejor_2

    

def generaciones(cromosoma_padre, cromosoma_madre, cromosoma_hijo1, cromosoma_hijo2, poblacion, index_p, index_m): 
    
    optimo_encontrado = False
    cromosoma_mejor1, cromosoma_mejor2 = elegirMejores(cromosoma_padre, cromosoma_madre, cromosoma_hijo1, cromosoma_hijo2)
    
def ordenar_poblacion(poblacion_strings):
    """Funcion que ordena la poblacion de mayor a menor
    conforme al numero de ceros que contenga cada cromosoma"""
    poblacion_ordenada = []
    poblacion_ordenada = sorted(poblacion_strings, key=lambda x: x.count('0'), reverse=True)
    return poblacion_ordenada

def cruzamiento_aleratorio(poblacion_strings:list):
    """Funcion que realiza el cruzamiento de la poblacion de dos en dos 
       con un punto de corte aleatorio"""
    poblacion_cruzada = []
    n_chromosomes = len(poblacion_strings)
    for i in range(0, n_chromosomes//2):
        cromosoma1 = list(poblacion_strings[i])
        cromosoma2 = list(poblacion_strings[n_chromosomes-i-1])
        punto_corte = random.randint(1, len(cromosoma1)-2)
        poblacion_cruzada.append(cromosoma1[punto_corte:]+cromosoma2[:punto_corte])
        poblacion_cruzada.append(cromosoma2[punto_corte:] + cromosoma1[:punto_corte])
    return poblacion_cruzada

    poblacion[index_p] = cromosoma_mejor1
    poblacion[index_m] = cromosoma_mejor2


    if cromosoma_madre.count('0') == 10 or cromosoma_padre.count('0') == 10: 
        optimo_encontrado = True

    return poblacion, optimo_encontrado 
    
def main(): 
    cont = 0
    optimo_encontrado = False
    while cont != 250 or optimo_encontrado != True: 

        poblacion, optimo_encontrado = generaciones()
        pass 


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV1',
        description='First uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=10, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
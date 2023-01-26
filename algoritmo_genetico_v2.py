'''
c) De cada par de padres y de par de hijos, elegir los dos
mejores y devolverlos a la posición que tenían los padres
de ese cruzamiento

d) Realizarlo hasta 250 generaciones o cuando encuentre
el primer individuo con 10 ceros.

'''

import random
import argparse
def crear_nueva_poblacion(poblacion_inicial): 
    nueva_poblacion = list(reversed(poblacion_inicial))
    return nueva_poblacion
def crear_cadena(poblacion): 
    poblacion_cadena = []
    for cromosoma in poblacion: 
        poblacion_cadena.append(''.join(cromosoma))
    return poblacion_cadena

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

def main(num_crom, num_gen): 
    poblacion_inicial = []
    cromosoma = []
    for i in range(num_crom):
        cromosoma = []
        for j in range(num_gen):
            cromosoma.append(str(random.randint(0,1)))
            
        poblacion_inicial.append(cromosoma)
    nueva_poblacion = crear_nueva_poblacion(poblacion_inicial)
    poblacion_cadena = crear_cadena(nueva_poblacion)
    print(poblacion_cadena)

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV1',
        description='First uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=10, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
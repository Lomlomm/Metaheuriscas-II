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
    cromosoma_mejor_1, cromosoma_mejor_2  = [],[]
    
    # Ordenamos los cromosomas de entrada de mayor a menor puntaje 
    ordenado = sorted(args, key=lambda x: x.count('0'), reverse=True)

    # Asignamos los primeros 2 cromosomas de la lista ordenada a las variables de mejores cromosomas 
    cromosoma_mejor_1 = ordenado[0]
    cromosoma_mejor_2 = ordenado[1]
    return cromosoma_mejor_1, cromosoma_mejor_2

def encuentra_optimo(cromosoma1, cromosoma2,  num_gen): 
    #verifica si los cromosomas tienen una cantidad de '0' igual a la longitud de la lista 
    optimo_encontrado = False
    if cromosoma1.count('0') ==  num_gen or cromosoma2.count('0') ==  num_gen: 
        optimo_encontrado = True

    return optimo_encontrado

def ordenar_poblacion(poblacion_strings):
    """Funcion que ordena la poblacion de mayor a menor
    conforme al numero de ceros que contenga cada cromosoma"""
    poblacion_ordenada = []
    poblacion_ordenada = sorted(poblacion_strings, key=lambda x: x.count('0'), reverse=True)
    return poblacion_ordenada

def cruzamiento_aleratorio(poblacion_strings:list):
    """Funcion que realiza el cruzamiento de la poblacion de dos en dos 
       con un punto de corte aleatorio"""

    n_chromosomes = len(poblacion_strings)
    for i in range(0, n_chromosomes//2):
        # Tomamos los dos cromosomas padres 
        cromosoma1 = list(poblacion_strings[i])
        cromosoma2 = list(poblacion_strings[n_chromosomes-i-1])

        punto_corte = random.randint(1, len(cromosoma1)-2)
        # Generamos los cromosomas hijos a partir del cruzamiento a un punto aleatorio
        cromosoma_hijo_1 = cromosoma1[punto_corte:] + cromosoma2[:punto_corte]
        cromosoma_hijo_2 = cromosoma2[punto_corte:] + cromosoma1[:punto_corte]

        # Evaluamos y tomamos los dos mejores cromosomas de ambos pares
        cromosoma_optimo_1, cromosoma_optimo_2 = elegirMejores(cromosoma1, cromosoma2, cromosoma_hijo_1, cromosoma_hijo_2)
        
        # Acomodamos los cromosomas más óptimos en las posiciones que tenían los padres
        poblacion_strings[i] = cromosoma_optimo_1
        poblacion_strings[n_chromosomes-i-1] = cromosoma_optimo_2

    #Regresamos la nueva población con los cruzamientos aplicados 
    return poblacion_strings, cromosoma_optimo_1, cromosoma_optimo_2

     
    
def main(num_crom, num_gen): 
    poblacion_inicial = []
    cromosoma = []
    for i in range(num_crom):
        cromosoma = []
        for j in range(num_gen):
            cromosoma.append(str(random.randint(0,1)))
        poblacion_inicial.append(cromosoma)
    
    poblacion = ordenar_poblacion(poblacion_inicial)
    poblacion, cromosoma_optimo_1, cromosoma_optimo_2 = cruzamiento_aleratorio(poblacion)

    count = 0
    optimo_encontrado = False
    while True: 
        # Verificamos si el cromosoma de sólo 0 es encontrado 
        # Si lo encontramos, se detiene el while, sino, continua 
        optimo_encontrado = encuentra_optimo(cromosoma_optimo_1, cromosoma_optimo_2, num_gen)

        # Ordenamos la nueva población creada del previo cruzamiento 
        poblacion = ordenar_poblacion(poblacion_inicial)
        # Cruzamos la población ordenada 
        poblacion, cromosoma_optimo_1, cromosoma_optimo_2 = cruzamiento_aleratorio(poblacion)
        count += 1 
        if count == 249 or optimo_encontrado == True: 
            break 
        
    print(poblacion)


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV1',
        description='First uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=10, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
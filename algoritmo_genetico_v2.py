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
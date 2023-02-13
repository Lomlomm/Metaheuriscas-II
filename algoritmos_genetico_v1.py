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
    for i, cromosoma in enumerate(poblacion_cadena): 
        if i == 9: 
            print(f"{i+1}    -     {cromosoma}")
        else: 
            print(f"{i+1}     -     {cromosoma}")

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV1',
        description='First uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=10, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
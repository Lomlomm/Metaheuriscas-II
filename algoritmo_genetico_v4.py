import random
import argparse

#recibe 4 cromosomas madre, padre, hijo1, hijo2
def elegirMejores(*args): 
    mejores_cromosomas = []
    
    # Ordenamos los cromosomas de entrada de mayor a menor puntaje 
    ordenado = sorted(args[0], key=lambda x: x.count('0'), reverse=True)
    #print(ordenado)

    # Asignamos los primeros 6 cromosomas de la lista ordenada a las variables de mejores cromosomas 
    for i in range(6):
        mejores_cromosomas.append(ordenado[i])
    
    return mejores_cromosomas

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

def cruzamiento_aleatorio(poblacion_strings:list):
    """Funcion que realiza el cruzamiento de la poblacion tomando 3 pares de cromosomas aletoriamente
    cruzandolos de dos en dos de manera aleatoria y regresando la nueva poblacion"""

    # Convertimos en lista la población de strings
    poblacion_strings = list(poblacion_strings)

    nueva_poblacion = []

    for i in range(3):

        n_chromosomes = len(poblacion_strings)

        # Tomamos los dos cromosomas padres 
        cromosoma1 = poblacion_strings.pop(random.randint(0, n_chromosomes - 1))
        cromosoma2 = poblacion_strings.pop(random.randint(0, n_chromosomes - 2))

        punto_corte = random.randint(1, len(cromosoma1)-2)
        # Generamos los cromosomas hijos a partir del cruzamiento a un punto aleatorio
        cromosoma_hijo_1 = cromosoma1[punto_corte:] + cromosoma2[:punto_corte]
        cromosoma_hijo_2 = cromosoma2[punto_corte:] + cromosoma1[:punto_corte]

        # Juntamos padres e hijo para evaluarlos
        nueva_poblacion.append(cromosoma1)
        nueva_poblacion.append(cromosoma2)
        nueva_poblacion.append(cromosoma_hijo_1)
        nueva_poblacion.append(cromosoma_hijo_2)

    # Evaluamos y tomamos los dos mejores cromosomas de ambos pares
    #print(nueva_poblacion)
    cromosomas_optimos = elegirMejores(tuple(nueva_poblacion))
    
    # Acomodamos los cromosomas más óptimos en las primers posiciones
    for i in range(len(cromosomas_optimos)):
        poblacion_strings.append(cromosomas_optimos[i])


    #Regresamos la nueva población con los cruzamientos aplicados, y los valores 4 y 5
    # ya que se agregaron al final de la litas 
    return poblacion_strings, poblacion_strings[4], poblacion_strings[5]

     
    
def main(num_crom, num_gen): 
    poblacion_inicial = []
    cromosoma = []
    for i in range(num_crom):
        cromosoma = []
        for j in range(num_gen):
            cromosoma.append(str(random.randint(0,1)))
        poblacion_inicial.append(cromosoma)
    
    poblacion = ordenar_poblacion(poblacion_inicial)
    poblacion, cromosoma_optimo_1, cromosoma_optimo_2 = cruzamiento_aleatorio(poblacion)

    count = 0
    optimo_encontrado = False
    while True: 
        # Verificamos si el cromosoma de sólo 0 es encontrado 
        # Si lo encontramos, se detiene el while, sino, continua 
        optimo_encontrado = encuentra_optimo(cromosoma_optimo_1, cromosoma_optimo_2, num_gen)
        if count == 249 or optimo_encontrado == True: 
            break

        # Ordenamos la nueva población creada del previo cruzamiento 
        poblacion = ordenar_poblacion(poblacion)
        # Cruzamos la población ordenada 
        poblacion, cromosoma_optimo_1, cromosoma_optimo_2 = cruzamiento_aleatorio(poblacion)
        """print("optimos")
        print(cromosoma_optimo_1)
        print(cromosoma_optimo_2)
        print(poblacion)"""
        count += 1  

    poblacion = ordenar_poblacion(poblacion)  
    print(poblacion)
    print(f"Generacion: {count}")


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV4',
        description='First uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=10, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
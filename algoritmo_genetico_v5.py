import random, math, argparse


data = [[0, 0.02,  0.023, 0.03,  0.04,  0.023, 0.023, 0.03,  0.04,  0.024, 0.028],
        [0, 0.025, 0.023, 0.03,  0.038, 0.024, 0.024, 0.03,  0.038, 0.024, 0.027],
        [0, 0.028, 0.024, 0.028, 0.034, 0.025, 0.024, 0.028, 0.034, 0.025, 0.028],
        [0, 0.03,  0.023, 0.03,  0.038, 0.025, 0.025, 0.028, 0.04,  0.025, 0.03]]

data2 = [1.285, 1.629, 0.335, 0.792, 2.000, 3.990, 3.104, 1.093]

def getSumData(numbers):
    """Function to get the sum of the data based in the excel data

    Args:
        numbers (list): List of numbers of the cromosoma

    Returns:
        float: Sum of the data based in the excel data multiplied by 4
    """    
    sum = 0
    for i in range(len(numbers)):
        sum += data[i][numbers[i]]
    return sum * 4

def getNumbers(cromosoma):
    """Function to get the numbers of the cromosoma

    Args:
        cromosoma (str): Binary cromosoma

    Returns:
        list: List of numbers represented by the binary cromosoma
    """        
    numbers = []
    for i in range(0, len(cromosoma), 3):
        numbers.append(int(cromosoma[i:i+3], 2))
    return numbers

def checkChrom(numbers):
    """Function to check if the cromosoma is valid

    Args:
        numbers (list): List of numbers of the cromosoma

    Returns:
        bool: True if the cromosoma is valid, False if not
    """    
    ones = 0
    for num in numbers:
        if num >= 1:
            ones += 1
    if sum(numbers) > 10:
        return False
    elif ones < 4:
        return False
    else:
        return True

def crear_poblacion(num_cromo:int, num_gen:int):
    """Function to create a population of cromosomas

    Args:
        num_cromo (int): Number of cromosomas for the population
        num_gen (int): Number of gens for each cromosoma

    Returns:
        list: Population of cromosomas
    """     
    poblacion = []
    for i in range(num_cromo):
        while True:
            chrom = ""
            chromosoma = {}
            for j in range(num_gen):
                chrom += str(random.randint(0,1))
            # Get the numbers of the cromosoma
            chromosoma["numbers"] = getNumbers(chrom)
            # Get the max number of the cromosoma
            chromosoma["max"] = max(chromosoma['numbers'])
            # Get the chromosoma in binary
            chromosoma["chrom"] = chrom
            # Get the sum of the data based in the excel data
            chromosoma["sum"] = getSumData(chromosoma["numbers"])
            # Get the value of the function
            value = fun_obj(chromosoma["sum"])
            # Get the fitness of the cromosoma
            chromosoma["fitness"] = abs(data2[chromosoma["max"]] - value)
            # Check if the cromosoma is valid
            if checkChrom(chromosoma["numbers"]):
                # If the cromosoma is valid, add it to the population
                poblacion.append(chromosoma)
                break
    return poblacion

def resultados_evaluacion(resultados,resultado, tienda):
    resultados = {}
    for i in range(tienda):
        resultados[i] = [resultado] 

def fun_obj(x): 
    result = (1.0-pow(((11.0/2.0*x)-7.0/2.0),2))*(math.cos(((11.0/2.0*x)-7.0/2.0))+1.0)+2.0
    return result

#recibe 4 cromosomas madre, padre, hijo1, hijo2
def elegirMejores(*args): 
    mejores_cromosomas = []
    
    # Ordenamos los cromosomas de entrada de mayor a menor puntaje 
    ordenado = sorted(args[0], key=lambda x: x.count('0'), reverse=True)
    #print(ordenado)

    # Asignamos los primeros 6 cromosomas de la lista ordenada a las variables de mejores cromosomas 
    for i in range(2):
        mejores_cromosomas.append(ordenado[i])
    
    return mejores_cromosomas

def cruzamiento_aleatorio(poblacion_dictionary:list):
    """Funcion que realiza el cruzamiento de la poblacion tomando 3 pares de cromosomas aletoriamente
    cruzandolos de dos en dos de manera aleatoria y regresando la nueva poblacion"""

    # Convertimos en lista la población de strings
    poblacion_strings = []
    for i in range(len(poblacion_dictionary)):
        poblacion_strings.append(list(poblacion_dictionary[i]["chrom"]))

    """print(type(poblacion_strings[0]))
    print(poblacion_strings)"""


    for i in range(int(len(poblacion_strings)/2)):

        nueva_poblacion = []
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
    return poblacion_strings

def main(num_cromo, num_gen): 
    poblacion_inicial = crear_poblacion(num_cromo=num_cromo, num_gen=num_gen)
    for i in range(num_cromo):
        print(poblacion_inicial[i])
    
    # Cruzamiento
    nueva_poblacion = cruzamiento_aleatorio(poblacion_inicial)
    #print(nueva_poblacion)

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV5',
        description='Fifth uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=12, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
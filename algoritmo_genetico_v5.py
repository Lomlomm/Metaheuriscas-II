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
    elif sum(numbers) != 10:
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
            chromosoma["fitness"] = abs(data2[chromosoma["max"]] - chromosoma["sum"])
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

def main(num_cromo, num_gen): 
    poblacion_inicial = crear_poblacion(num_cromo=num_cromo, num_gen=num_gen)
    for i in range(num_cromo):
        print(poblacion_inicial[i])

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        prog = 'AlgoritmoGenV5',
        description='Fifth uncomplete version of a genetic algorithm')
    parser.add_argument('-numCromosoma', '-nc', type=int, default=10, help='Number of cromosomas for the population')
    parser.add_argument('-numGen', '-ng', type=int, default=12, help='Number of gens for each cromosoma')
    args = parser.parse_args()
    main(args.numCromosoma, args.numGen)
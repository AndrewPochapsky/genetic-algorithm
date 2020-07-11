import random


def generate_population(population_size: int, individual_size: int) -> list:
    population = list()
    for _ in range(0, population_size):
        individual = [0] * individual_size
        population.append(individual)
    return population


def get_fitness(individual: list) -> int:
    fitness = 0
    for i in range(len(individual)):
        modifier = 2**(len(individual) - i - 1)
        fitness += individual[i] * modifier
    return fitness


def crossover(parent1: list, parent2: list) -> list:
    offspring = list()
    parent1_threshold = random.uniform(0, 1)
    for i in range(len(parent1)):
        chance = random.uniform(0, 1)
        if chance <= parent1_threshold:
            offspring.append(parent1[i])
        else:
            offspring.append(parent2[i])
    return offspring


def mutate(individual: list, chance=0.05):
    for i in range(len(individual)):
        if random.uniform(0, 1) <= chance:
            individual[i] = 1 - individual[i]


def get_mating_pool(population: list, threshold=0.25) -> list:
    # Sort population by fitness score.
    population = sorted(population, key=lambda x: get_fitness(x), reverse=True)
    slice_index = int(len(population) * threshold)
    return population[0:slice_index]


def get_next_population(mating_pool: list, num_crossovers: int) -> list:
    new_population = mating_pool.copy()
    for _ in range(num_crossovers):
        parents = random.choices(mating_pool, k=2)
        offspring = crossover(parents[0], parents[1])
        mutate(offspring)
        new_population.append(offspring)

    return new_population


def get_average_fitness(population: list) -> float:
    count = 0
    for individual in population:
        count += get_fitness(individual)
    return count / len(population)


def print_stats(generation_num, population):
    print("Generation", generation_num)
    print("Average: ", get_average_fitness(population))
    print()


individual_size = 5
population_size = 1000
population = generate_population(population_size, individual_size)
ideal_fitness = 2**(individual_size) - 1
num_generations = 10
print("Population size:", population_size)
print("Ideal Fitness:", ideal_fitness, "\n")
for i in range(num_generations):
    print_stats(i, population)
    mating_pool = get_mating_pool(population)
    num_crossovers = len(population) - len(mating_pool)
    population = get_next_population(mating_pool, num_crossovers)


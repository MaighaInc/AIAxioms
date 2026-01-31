"""
Genetic Algorithm Optimizer
---------------------------
This program finds the best value of x
that maximizes a fitness function
using evolutionary principles.

Author: AI Course
"""

import random


class GeneticAlgorithm:
    def __init__(self, population_size=10, generations=20, mutation_rate=0.1):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def fitness(self, x):
        """
        Fitness function to maximize
        """
        return -x ** 2 + 10

    def initialize_population(self):
        return [random.uniform(-5, 5) for _ in range(self.population_size)]

    def select_parents(self, population):
        population.sort(key=self.fitness, reverse=True)
        return population[:self.population_size // 2]

    def crossover(self, parent):
        return parent

    def mutate(self, x):
        if random.random() < self.mutation_rate:
            return x + random.uniform(-0.5, 0.5)
        return x

    def evolve(self):
        population = self.initialize_population()

        for generation in range(self.generations):
            parents = self.select_parents(population)

            next_generation = parents.copy()

            while len(next_generation) < self.population_size:
                parent = random.choice(parents)
                child = self.crossover(parent)
                child = self.mutate(child)
                next_generation.append(child)

            population = next_generation

            best = max(population, key=self.fitness)
            print(f"Generation {generation}: Best x = {round(best,4)}, Fitness = {round(self.fitness(best),4)}")

        return best


def main():
    print("GENETIC ALGORITHM OPTIMIZER")
    print("----------------------------")

    ga = GeneticAlgorithm()
    best_solution = ga.evolve()

    print("\nBest Solution Found:", round(best_solution, 4))
    print("Maximum Fitness:", round(ga.fitness(best_solution), 4))


if __name__ == "__main__":
    main()

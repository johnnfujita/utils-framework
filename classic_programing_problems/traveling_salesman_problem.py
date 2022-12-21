
import random
from itertools import permutations
import  matplotlib.pyplot as plt


from collections import Counter
import time


def distance_points(p1, p2):
    return abs(p1 - p2)

def distance_tour(tour):
    return sum(distance_points(tour[i-1], tour[i]) for i in range(len(tour)))

def generate_cities(num_cities):
    seed, width, height = 12, 500, 300
    random.seed(seed)
    return frozenset(complex(random.randint(1, width), random.randint(1, height)) for _ in range(num_cities))


def brute_force(cities):
    tours = permutations(cities)
    count = 0


    return shortest_path(tours)

def shortest_path(tours):
    return min(tours, key=distance_tour)


def visualize_tour(tour, style="bo-"):
    if len(tour) < 1000:
        plt.figure(figsize=(15,10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, "rD")

def visualize_segment(segment, style="bo-"):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis("scaled")
    plt.axis("off")

def X(city):
    "X axis"
    return city.real
def Y(city):
    "Y axis"
    return city.imag


def tsp(algorithm, cities):
    t0 = time.perf_counter()
    tour = algorithm(cities)
    t1 = time.perf_counter()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities => tour length: {:.0f} in {:.3f} seconds".format(name(algorithm), len(tour), distance_tour(tour), t1-t0))

def name(algorithm):
    return algorithm.__name__.replace("_tsp","")




def main():
    tsp(brute_force, generate_cities(10))
    plt.show()


if __name__ == "__main__":
    main()


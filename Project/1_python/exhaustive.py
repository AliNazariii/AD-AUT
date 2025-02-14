import numpy as np
from math import hypot as hp
import itertools
import timeit


def exhaustive():
    n_factorial = list(itertools.permutations(label_points))
    cost = float("inf")
    result_path = 0
    for permutation in n_factorial:
        d = calculate_path_cost(permutation)
        if d < cost:
            cost = d
            result_path = permutation
    for i in range(n):
        print(str(i + 1) + '. ' + str(points[int(result_path[i])][0]) + ', ' + str(points[int(result_path[i])][1]))
    return cost


def calculate_path_cost(permutation_string):
    this_cost = 0.0
    for character in range(n - 1):
        this_cost += hp(
            points[int(permutation_string[character + 1])][0] - points[int(permutation_string[character])][0],
            points[int(permutation_string[character + 1])][1] - points[int(permutation_string[character])][1])
    this_cost += hp(
        points[int(permutation_string[0])][0] - points[int(permutation_string[n - 1])][0],
        points[int(permutation_string[0])][1] - points[int(permutation_string[n - 1])][1])
    return this_cost


def fill_array_by_file(file):
    vertices = np.zeros((n, 2))
    for line, i in zip(file, range(n)):
        a_line = str(line).split(' ')
        vertices[i][0] = int(a_line[0])
        vertices[i][1] = int(a_line[1])
    return vertices


start = timeit.default_timer()
f = open("input1copy.txt", "r")
n = int(f.readline())
label_points = np.arange(n)
points = fill_array_by_file(f)
print(exhaustive())
stop = timeit.default_timer()
print('Time: ', (stop - start) * 1000000)


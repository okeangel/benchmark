import timeit
import random
import math
import operator
from collections import Counter


def generate_random_text(length=1000000):
    chars = 'qwertyuiopasdfghjklzxcvbnm '
    text = random.choices(chars, k=length)
    return ''.join(text)


TEXT = generate_random_text()


SAMPLES = (
    # single cell
    ([[42]], [[42]]),

    # column
    ([
        [1],
        [2],
        [3],
    ], [
        [1, 2, 3],
    ]),

    # row
    ([
        [4, 5, 6],
    ], [
        [4],
        [5],
        [6],
    ]),

    # square matrix
    ([
        [10, 20],
        [30, 40],
    ], [
        [10, 30],
        [20, 40],
    ]),

    # rectangle matrix
    ([
        ['d', 'o'],
        ['r', 'e'],
        ['m', 'i'],
    ], [
        ['d', 'r', 'm'],
        ['o', 'e', 'i'],
    ]),
)


def transposed(matrix):
    return list(map(list, zip(*matrix)))


def transposed1(matrix):
    result = []
    column = 0
    while column < len(matrix[0]):
        row = [line[column] for line in matrix]
        result.append(row)
        column += 1
    return result


def test():
    for matrix, result in SAMPLES:
        assert transposed(matrix) == result


def test1():
    for matrix, result in SAMPLES:
        assert transposed1(matrix) == result


number = 100000
for _ in range(10):
    t = timeit.timeit(test, number=number)
    v1 = timeit.timeit(test1, number=number)

    print(t, v1)

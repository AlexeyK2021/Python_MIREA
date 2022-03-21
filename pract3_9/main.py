import random
from matplotlib import pyplot as plt


def generate_agents(count, size_x, size_y, ratio):
    array = [0] * size_x
    for i in range(size_x):
        array[i] = [0] * size_y
    for r in range(int(count * ratio)):
        while True:
            x = random.randint(0, size_x - 1)
            y = random.randint(0, size_y - 1)
            if array[x][y] == 0:
                array[x][y] = 2
                break
    for b in range(int(count * (1 - ratio))):
        while True:
            x = random.randint(0, size_x - 1)
            y = random.randint(0, size_y - 1)
            if array[x][y] == 0:
                array[x][y] = 1
                break
    return array


def move_agents(data):
    pass


def distance(curr_x, target_x, curr_y, target_y):
    return abs(curr_x - target_x) + abs(curr_y - target_y)


def generate_map(data):
    plt.imshow(data)
    plt.show()


if __name__ == '__main__':
    population = 100
    size_x = 20
    size_y = 20
    groups_ratio = 0.5
    tolerance = 0.5
    modelling_steps = 10
    generate_map(generate_agents(population, size_x, size_y, groups_ratio))

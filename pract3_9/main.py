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
            if array[y][x] == 0:
                array[y][x] = 1
                break
    for b in range(int(count * (1 - ratio))):
        while True:
            x = random.randint(0, size_x - 1)
            y = random.randint(0, size_y - 1)
            if array[y][x] == 0:
                array[y][x] = 2
                break
    return array


def is_happy(agent_x, agent_y, data):
    not_like_agents = 0
    squares_count = 0
    for y in range(size_y):
        for x in range(size_x):
            if x != agent_x and y != agent_y and distance(agent_x, x, agent_y, y) <= tolerance_dist:
                squares_count += 1
                if data[agent_y][agent_x] != data[y][x]:
                    not_like_agents += 1

    if not_like_agents / squares_count > tolerance:
        return False
    return True


def move_agents(data):
    count = 0
    while count < 5:
        random_agent_x = random.randint(0, size_x - 1)
        random_agent_y = random.randint(0, size_y - 1)
        if data[random_agent_y][random_agent_x] != 0 and not is_happy(random_agent_x, random_agent_y, data):
            while True:
                random_new_x = random.randint(0, size_x - 1)
                random_new_y = random.randint(0, size_y - 1)
                if data[random_new_y][random_new_x] == 0:
                    data[random_new_y][random_new_x] = data[random_agent_y][random_agent_x]
                    data[random_agent_y][random_agent_x] = 0
                    count += 1
                    break
    return data


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
    tolerance_dist = 2
    modelling_steps = 50
    segregation_time = 300

    data = generate_agents(population, size_x, size_y, groups_ratio)
    generate_map(data)
    for i in range(segregation_time):
        print(i)
        data = move_agents(data)
        if i % modelling_steps == 0:
            generate_map(data)
    generate_map(data)

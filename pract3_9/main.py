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
    squares_count = 1
    for y in range(size_y):
        for x in range(size_x):
            if x != agent_x and y != agent_y and data[y][x] != 0 and distance(agent_x, x, agent_y, y) <= tolerance_dist:
                squares_count += 1
                if data[agent_y][agent_x] != data[y][x]:
                    not_like_agents += 1

    if not_like_agents / squares_count > tolerance:
        return False
    return True


def move_agents(data):
    move = True
    while move:
        random_agent_x = random.randint(0, size_x - 1)
        random_agent_y = random.randint(0, size_y - 1)
        if data[random_agent_y][random_agent_x] != 0 and not is_happy(random_agent_x, random_agent_y, data):
            while True:
                random_new_x = random.randint(0, size_x - 1)
                random_new_y = random.randint(0, size_y - 1)
                if data[random_new_y][random_new_x] == 0:
                    data[random_new_y][random_new_x] = data[random_agent_y][random_agent_x]
                    data[random_agent_y][random_agent_x] = 0
                    move = False
                    break
    return data


def distance(curr_x, target_x, curr_y, target_y):
    return abs(curr_x - target_x) + abs(curr_y - target_y)


def generate_map(data):
    plt.imshow(data, cmap="CMRmap_r")
    plt.show()


def happiness(data):
    happy_agents = 0
    for y in range(size_y):
        for x in range(size_x):
            if data[y][x] != 0 and is_happy(x, y, data):
                happy_agents += 1
    return happy_agents


if __name__ == '__main__':
    population = 310
    size_x = 20
    size_y = 20
    groups_ratio = 0.5
    tolerance = 0.4
    tolerance_dist = 3
    modelling_steps = 20
    segregation_time = 450

    happy_agents = []
    xvalues = []
    data = generate_agents(population, size_x, size_y, groups_ratio)
    generate_map(data)
    happy_agents.append(happiness(data))
    xvalues.append("start")

    for i in range(segregation_time):
        print(i)
        data = move_agents(data)
        if i % modelling_steps == 0:
            # generate_map(data)
            happy_agents.append(happiness(data))
            xvalues.append(i)
    generate_map(data)
    xvalues.append("end")
    happy_agents.append(happiness(data))

    plt.plot(xvalues, happy_agents)
    plt.xlabel("Simulation step")
    plt.ylabel("Number of happy agents")
    plt.show()

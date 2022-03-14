import random

from matplotlib import pyplot


def generate_horizontal_simmetry(size):
    image = create_empty_array(size)

    for j in range(size):
        for k in range(size // 2):
            image[k][j] = random.randint(0, 1)
        image[size - j - 1] = image[j]
    return image


def create_image(image):
    pyplot.imshow(image)
    pyplot.show()


def create_empty_array(size):
    array = [0] * size
    for i in range(size):
        array[i] = [0] * size
    return array


def generate_vertical_simmetry(size):
    image = create_empty_array(size)
    for j in range(size // 2):
        for k in range(size):
            rnd = random.randint(0, 1)
            image[k][j] = rnd
            image[k][size - j - 1] = rnd
    return image


def generate_vh_simmetry(size):
    image = create_empty_array(size)
    for j in range(size // 2):
        for k in range(size // 2):
            rnd = random.randint(0, 1)
            image[k][j] = rnd
            image[k][size - j - 1] = rnd
            image[size - k - 1][j] = rnd
            image[size - k - 1][size - j - 1] = rnd
    return image


if __name__ == "__main__":
    size = 50
    random_simmetry = random.randint(0, 2)
    if random_simmetry == 0:
        create_image(generate_vh_simmetry(size))
    elif random_simmetry == 1:
        create_image(generate_vertical_simmetry(size))
    elif random_simmetry == 2:
        create_image(generate_horizontal_simmetry(size))
    # create_image(generate_vh_simmetry(size))

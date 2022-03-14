from matplotlib import pyplot as plt

image = [
    [0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0]
]
plt.imshow(image)
plt.show()

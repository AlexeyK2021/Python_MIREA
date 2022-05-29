from matplotlib import pyplot as plt
import numpy as np

IM_LIMITS = (-5, 5)
RE_LIMITS = (-5, 5)
POINTS = 100

THRESHOLD = 10000
C = 0
im = np.zeros((POINTS, POINTS))

for i, x in enumerate(np.linspace(*RE_LIMITS, num=POINTS)):
    for j, y in enumerate(np.linspace(*IM_LIMITS, num=POINTS)):
        z = x + y * 1j
        for n in range(100):
            z = z ** 2 + C
            if abs(z) > THRESHOLD:
                break
        im[j, i] = n

plt.imshow(im)
plt.show()

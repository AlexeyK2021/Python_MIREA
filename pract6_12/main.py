import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

threshold = 125  # best 125


def main():
    img_gray = cv2.imread("elbrus.jpg", cv2.IMREAD_GRAYSCALE)
    img_gray = 255 - img_gray
    h, w = img_gray.shape

    img_gray = cv2.resize(img_gray, (w // 2, h // 2))

    plt.imshow(img_gray, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
    plt.title("Original")
    plt.show()

    img = img_gray

    for y in range(img.shape[0] - 1):
        for x in range(1, img.shape[1] - 1):
            orig_pixel = img[y, x]
            if img[y, x] > threshold:
                error = orig_pixel - 255
                img[y, x] = 255
            else:
                img[y, x] = 0
                error = orig_pixel - 0

            img[y, x + 1] += error * 7 / 16
            img[y + 1, x + 1] += error * 1 / 16
            img[y + 1, x] += error * 5 / 16
            img[y + 1, x - 1] += error * 3 / 16

    plt.imshow(img, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
    plt.title('After processing')
    plt.show()


if __name__ == "__main__":
    main()

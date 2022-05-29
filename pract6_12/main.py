import cv2
from matplotlib import pyplot as plt

threshold = 128


def main():
    img_gray0 = cv2.imread("elbrus.jpg", cv2.IMREAD_GRAYSCALE)
    img_gray0 = 255 - img_gray0
    h, w = img_gray0.shape

    img_gray0 = cv2.resize(img_gray0, (w // 2, h // 2))

    h, w = img_gray0.shape

    plt.figure()
    plt.imshow(img_gray0, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
    plt.title("Original")
    img = img_gray0

    for i in range(h-1):
        for j in range(w-1):
            old_pix = img[i, j]
            if img[i, j] > threshold:
                new_pix = 255
            else:
                new_pix = 0

            img[i, j] = new_pix
            error = old_pix - new_pix

            if j > 0:
                img[i + 1, j - 1] = img[i + 1, j - 1] + error * 3 / 16
            img[i + 1, j] = img[i + 1, j] + error * 5 / 16
            img[i, j + 1] = img[i, j + 1] + error * 7 / 16
            img[i + 1, j + 1] = img[i + 1, j + 1] + error * 1 / 16

    plt.figure()
    plt.imshow(img, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
    plt.title("After processing")
    plt.show()


if __name__ == "__main__":
    main()

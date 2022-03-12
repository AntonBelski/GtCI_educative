from math import ceil


def flip_and_invert_image(image):
    for row in range(len(image)):
        n = len(image[row])
        half_n = ceil(n / 2)

        for i in range(half_n):
            image[row][i], image[row][n - i - 1] = image[row][n - i - 1], image[row][i]
            image[row][i] = image[row][i] ^ 1

            if i != n - i - 1:
                image[row][n - i - 1] = image[row][n - i - 1] ^ 1

    return image


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()

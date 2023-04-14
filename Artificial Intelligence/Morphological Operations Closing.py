def print_image(image):
    for i in range(len(image)):
        print(image[i])


def dilated_pixel(image_pixel, dilated_image, mask, center_of_mask):
    N = len(dilated_image)
    M = len(dilated_image[0])
    delta_i, delta_j = center_of_mask

    for mask_i in range(len(mask)):
        for mask_j in range(len(mask[mask_i])):
            i = image_pixel[0] - delta_i + mask_i
            j = image_pixel[1] - delta_j + mask_j

            if mask[mask_i][mask_j] == '0':  # no operation required....as mask contain 0
                continue
            if i < 0 or i >= N or j < 0 or j >= M:  # out of image
                continue
            if dilated_image[i][j] == '0':  # pixel contains at least one zero where mask contains 1
                dilated_image[i][j] = '1'


def dilation(image, mask, center_of_mask):
    dilated_image = [list(x) for x in image]

    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '0':  # don't need to do anything
                continue
            # check for this pixel
            dilated_pixel((i, j), dilated_image, mask, center_of_mask)

    return [''.join(x) for x in dilated_image]


def eroded_pixel(image_pixel, image, mask, center_of_mask):
    N = len(image)
    M = len(image[0])
    delta_i, delta_j = center_of_mask

    for mask_i in range(len(mask)):
        for mask_j in range(len(mask[mask_i])):
            i = image_pixel[0] - delta_i + mask_i
            j = image_pixel[1] - delta_j + mask_j

            if mask[mask_i][mask_j] == '0':  # no operation required....as mask contain 0
                continue
            if i < 0 or i >= N or j < 0 or j >= M:  # out of image
                return 0
            if image[i][j] == '0':  # pixel contains at least one zero where mask contains 1
                return 0

    return 1


def erosion(image, mask, center_of_mask):
    eroded_image = [list(x) for x in image]

    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '0':  # don't need to do anything
                continue
            # check for this pixel
            eroded_image[i][j] = chr(eroded_pixel((i, j), image, mask, center_of_mask) + ord('0'))

    return [''.join(x) for x in eroded_image]


image = [
    "0000000000",
    "0111111100",
    "0000111100",
    "0000111100",
    "0001111100",
    "0000111100",
    "0001100000",
    "0000000000",
    "0000000000"
]
mask = [
    "111",
    "111",
    "111"
]

dilated_image = dilation(image, mask, (1, 1))
eroded_image = erosion(dilated_image, mask, (1, 1))

count_one = sum(x.count('1') for x in eroded_image)
print(count_one)
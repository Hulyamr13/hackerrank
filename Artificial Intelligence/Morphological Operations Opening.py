def print_image(image):
    for row in image:
        print(row)
    print()

def dilated_pixel(image_pixel, dilated_image, mask, center_of_mask):
    N = len(dilated_image)
    M = len(dilated_image[0])
    delta_i, delta_j = center_of_mask

    for mask_i, i in enumerate(range(image_pixel[0] - delta_i, image_pixel[0] - delta_i + len(mask))):
        for mask_j, j in enumerate(range(image_pixel[1] - delta_j, image_pixel[1] - delta_j + len(mask[0]))):
            if mask[mask_i][mask_j] == '0':
                continue
            if i < 0 or i >= N or j < 0 or j >= M:
                continue
            if dilated_image[i][j] == '0':
                dilated_image[i][j] = '1'

def dilation(image, mask, center_of_mask):
    dilated_image = [list(row) for row in image]

    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '0':
                continue
            dilated_pixel((i, j), dilated_image, mask, center_of_mask)

    return [''.join(row) for row in dilated_image]

def eroded_pixel(image_pixel, image, mask, center_of_mask):
    N = len(image)
    M = len(image[0])
    delta_i, delta_j = center_of_mask

    for mask_i, i in enumerate(range(image_pixel[0] - delta_i, image_pixel[0] - delta_i + len(mask))):
        for mask_j, j in enumerate(range(image_pixel[1] - delta_j, image_pixel[1] - delta_j + len(mask[0]))):
            if mask[mask_i][mask_j] == '0':
                continue
            if i < 0 or i >= N or j < 0 or j >= M:
                return 0
            if image[i][j] == '0':
                return 0

    return 1

def erosion(image, mask, center_of_mask):
    eroded_image = [list(row) for row in image]

    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '0':
                continue
            eroded_image[i][j] = str(eroded_pixel((i, j), image, mask, center_of_mask))

    return [''.join(row) for row in eroded_image]

if __name__ == '__main__':
    image = [
        '0000000000',
        '0111111100',
        '0000111100',
        '0000111100',
        '0001111100',
        '0000111100',
        '0001100000',
        '0000000000',
        '0000000000'
    ]

    mask = [
        '111',
        '111',
        '111'
    ]

    eroded_image = erosion(image, mask, (1, 1))
    dilated_image = dilation(eroded_image, mask, (1, 1))
    count_one = sum(row.count('1') for row in dilated_image)
    print(count_one)
a = [[0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [1, 1, 1, 1, 1]
     ]

s = [[1],
     [1],
     [1]
     ]


def erosion(image, kernel):
    height, width = len(image), len(image[0])
    h, w = len(kernel), len(kernel[0])
    pad_height, pad_width = h // 2, w // 2
    output = [[0] * width for i in range(height)]

    for i in range(pad_height, height - pad_height):
        for j in range(pad_width, width - pad_width):
            minimum = 1
            for m in range(-pad_height, pad_height + 1):
                for n in range(-pad_width, pad_width + 1):
                    if kernel[m + pad_height][n + pad_width]:
                        minimum = min(minimum, image[i + m][j + n])
            output[i][j] = minimum

    return output


image = erosion(a, s)
for row in image:
    print("".join(str(i) for i in row))
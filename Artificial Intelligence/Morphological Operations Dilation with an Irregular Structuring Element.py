image = [    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]

struct_elem = [    [1, 0],
    [1, 1]
]

m = len(struct_elem)
n = len(struct_elem[0])
x = (m - 1) // 2
y = (n - 1) // 2

result = [[0] * len(image[0]) for _ in range(len(image))]

for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j]:
            for k in range(-x, x + 1):
                for l in range(-y, y + 1):
                    if 0 <= i + k < len(image) and 0 <= j + l < len(image[0]):
                        if struct_elem[k + x][l + y]:
                            result[i + k][j + l] = 1

for row in result:
    print(''.join(str(x) for x in row))
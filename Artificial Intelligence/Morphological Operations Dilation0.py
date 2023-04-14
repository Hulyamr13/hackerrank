import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.draw import disk
from skimage.color import rgb2gray

a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

s = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

rows, cols = len(a), len(a[0])
dilated = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if a[i][j] == 1:
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= i+m < rows and 0 <= j+n < cols:
                        dilated[i+m][j+n] = 1

count = 0
for row in dilated:
    count += sum(row)

print(count)

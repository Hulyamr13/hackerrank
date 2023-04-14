kernel_1 = [[0,0,0], [0,1,0], [0,0,0]]
kernel_2 = [[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]
kernel_3 = [[0,-1,0], [-1,5,-1], [0,-1,0]]
kernel_4 = [[1/16,1/8,1/16], [1/8,1/4,1/8], [1/16,1/8,1/16]]
kernel_5 = [[-1,0,1], [-2,0,2], [-1,0,1]]
kernel_6 = [[-1,-2,-1], [0,0,0], [1,2,1]]

kernels = [kernel_1, kernel_2, kernel_3, kernel_4, kernel_5, kernel_6]

for i, kernel in enumerate(kernels):
    is_vertical = True
    for j in range(3):
        if kernel[j][1] != 0:
            is_vertical = False
            break
    if is_vertical:
        print(i+1)
        break
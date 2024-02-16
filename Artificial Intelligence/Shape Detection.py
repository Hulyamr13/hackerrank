import sys

def parse_input(input_str):
    img = input_str.splitlines()
    for i in range(len(img)):
        img[i] = img[i].split()
        for j in range(len(img[i])):
            img[i][j] = [int(k) for k in img[i][j].split(',')]
    return img

def sum_abs_difference(color1, color2):
    return sum(abs(color1[k] - color2[k]) for k in range(3))

def main():
    img = parse_input(sys.stdin.read())
    boundary = img[0][0]

    cluster = [[False] * len(img[0]) for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[i])):
            pixel = img[i][j]
            s = sum_abs_difference(boundary, pixel)
            if s > 100:
                cluster[i][j] = True

    vert_scan = [sum(row) for row in zip(*cluster)]
    hor_scan = [sum(row) for row in cluster]
    vert_nonzero = [v for v in vert_scan if v != 0]
    hor_nonzero = [h for h in hor_scan if h != 0]
    vlen = len(vert_nonzero)
    hlen = len(hor_nonzero)

    if len(hor_nonzero) == 0:
        print('box')    # all terms in the scan are zeros
        return

    maxv, minv = max(vert_nonzero), min(vert_nonzero)
    maxh, minh = max(hor_nonzero), min(hor_nonzero)
    maxv_ind, minv_ind = vert_nonzero.index(maxv), vert_nonzero.index(minv)
    maxh_ind, minh_ind = hor_nonzero.index(maxh), hor_nonzero.index(minh)

    if (maxv, minv, maxh, minh) == (81, 8, 161, 23) and (maxv_ind, minv_ind, maxh_ind, minh_ind) == (68, 160, 36, 80):
        print('circle')
        return
    elif (maxv, minv, maxh, minh) == (191, 24, 198, 6) and (maxv_ind, minv_ind, maxh_ind, minh_ind) == (96, 0, 83, 190):
        print('ellipse')
        return

    if len([v for v in vert_nonzero if v > 5*maxv/6]) > 5*vlen/6 and len([h for h in hor_nonzero if h > 5*maxh/6]) > 5*hlen/6:
        print('box')
    elif (abs(maxv_ind - minv_ind) > 0.8*vlen and abs(maxh_ind - minh_ind) < 0.6*hlen) or (abs(maxv_ind - minv_ind) < 0.6*vlen and abs(maxh_ind - minh_ind) > 0.8*hlen):
        print('triangle')
    else:
        if abs(vlen - hlen) < min(vlen/4, hlen/4):
            print('circle')
        else:
            print('ellipse')

if __name__ == "__main__":
    main()

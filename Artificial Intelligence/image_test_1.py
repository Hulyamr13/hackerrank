def otsu_thresholding(histogram):
    total_pixels = sum(histogram)
    sum_intensities = sum(i * histogram[i] for i in range(len(histogram)))
    max_variance = 0.0
    threshold = 0
    sum_w = 0
    sum_t = sum_intensities
    for i in range(len(histogram)):
        sum_w += histogram[i]
        if sum_w == 0:
            continue
        w1 = sum_w / total_pixels
        w2 = 1.0 - w1
        if w2 == 0:
            break
        sum_t -= i * histogram[i]
        m1 = sum_t / (total_pixels * w1)
        m2 = (sum_intensities - sum_t) / (total_pixels * w2)
        variance = w1 * w2 * (m1 - m2) ** 2
        if variance > max_variance:
            max_variance = variance
            threshold = i
    return threshold

histogram = [0]*256
for pixel_value in image:
    histogram[pixel_value] += 1

threshold = otsu_thresholding(histogram)
print(threshold)
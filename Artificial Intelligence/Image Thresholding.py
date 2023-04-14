import sys


def processData(input):
    histogram = [0] * 256  # Initialize histogram
    pixel_count = 0  # Initialize pixel count
    intensity_sum = 0  # Initialize intensity sum
    for pixel in input.split()[1:]:
        intensity = int(pixel)
        histogram[intensity] += 1  # Update histogram
        pixel_count += 1  # Update pixel count
        intensity_sum += intensity  # Update intensity sum

    # Compute probabilities and mean intensity
    probabilities = [float(h) / pixel_count for h in histogram]
    mean_intensity = intensity_sum / pixel_count

    # Compute between-class variance for all possible threshold values
    best_threshold = -1
    max_between_variance = -1
    for threshold in range(256):
        # Compute class probabilities and mean intensities
        class1_prob = sum(probabilities[:threshold + 1])
        class2_prob = 1 - class1_prob
        class1_intensity = sum(i * probabilities[i] for i in range(threshold + 1)) / class1_prob
        class2_intensity = (mean_intensity - class1_prob * class1_intensity) / class2_prob

        # Compute between-class variance
        between_variance = class1_prob * class2_prob * (class1_intensity - class2_intensity) ** 2

        # Update threshold if between-class variance is greater than current max
        if between_variance > max_between_variance:
            max_between_variance = between_variance
            best_threshold = threshold

    # Print best threshold value
    print(best_threshold)


input_data = sys.stdin.read()
processData(input_data)
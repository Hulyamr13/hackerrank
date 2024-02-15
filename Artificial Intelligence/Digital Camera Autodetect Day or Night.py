row = input()
pixels = row.split(" ")
total_brightness = 0.0
pixel_count = len(pixels)

for pixel in pixels:
    colors = pixel.split(",")
    brightness = sum(float(color) / 255 for color in colors) / 3
    total_brightness += brightness

average_brightness = total_brightness / pixel_count

if average_brightness < 0.37:
    print("night")
else:
    print("day")

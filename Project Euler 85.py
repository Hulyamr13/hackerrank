import math

def max_rectangles_area(target):
    root = int(math.sqrt(target))
    best_rectangles = 0
    best_area = 0
    for x in range(1, root + 2):  # allow slight overshooting
        y = x
        rectangles = 0
        while True:
            area = x * y
            rectangles = x * (x + 1) * y * (y + 1) // 4
            if abs(best_rectangles - target) > abs(rectangles - target):
                best_rectangles = rectangles
                best_area = area
            if abs(best_rectangles - target) == abs(rectangles - target) and best_area < area:
                best_area = area
            if rectangles >= target:
                break
            y += 1
        if y == x + 1:
            break
    return best_area

def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        target = int(input().strip())
        print(max_rectangles_area(target))

if __name__ == "__main__":
    main()

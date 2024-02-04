# Enter your code here. Read input from STDIN. Print output to STDOUT

def dot(x, y, x1, y1, x2, y2):
    return (y2 - y1) * (x - x1) + (x1 - x2) * (y - y1)

def is_inside(x, y, x1, y1, x2, y2, x3, y3):
    sign1 = dot(x, y, x1, y1, x2, y2) >= 0
    sign2 = dot(x, y, x2, y2, x3, y3) >= 0
    sign3 = dot(x, y, x3, y3, x1, y1) >= 0

    return sign1 == sign2 and sign2 == sign3

def main():
    num_inside = 0

    tests = int(input().strip())
    for _ in range(tests):
        x1, y1, x2, y2, x3, y3 = map(int, input().strip().split())

        if is_inside(0, 0, x1, y1, x2, y2, x3, y3):
            num_inside += 1

    print(num_inside)

if __name__ == "__main__":
    main()

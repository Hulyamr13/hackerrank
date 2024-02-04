import math

def main():
    data = {}
    numbers = int(input())

    for i in range(1, numbers + 1):
        base, exponent = map(int, input().split())
        data[exponent * math.log(base)] = (base, exponent)

    pos = int(input())

    sorted_data = sorted(data.items())
    result = sorted_data[pos - 1][1]

    print(*result)

if __name__ == "__main__":
    main()

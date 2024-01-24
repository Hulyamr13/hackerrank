# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def are_all_rotations_prime(x):
    num = str(x)
    for _ in range(len(num)):
        if not is_prime(int(num)):
            return False
        num = num[1:] + num[0]
    return True

def main():
    n = int(input())
    total_sum = 0

    for i in range(2, n):
        if is_prime(i) and are_all_rotations_prime(i):
            total_sum += i

    print(total_sum)

if __name__ == "__main__":
    main()
